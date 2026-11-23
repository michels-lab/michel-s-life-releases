"""Offline failures and dynamic-version tests; no GitHub calls or user data."""
import hashlib,importlib.util,tempfile,unittest
from pathlib import Path

HERE=Path(__file__).parent
spec=importlib.util.spec_from_file_location("latest",HERE/"verify_latest_life_release.py")
v=importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def fixture(windows=231,android=20):
    w=f"3.0.{windows}";a=f"0.2.{android}"
    names=(
        f"MichelsLife-Setup-v{w}.exe", f"MichelsLife-Setup-v{w}.exe.sha256",
        f"MichelsLife-Portable-v{w}.exe", f"MichelsLife-Portable-v{w}.exe.sha256",
        f"MichelsLife-v{w}.exe", f"MichelsLife-v{w}.exe.sha256",
        f"MichelsLife-Android-Direct-v{a}.apk",
        f"MichelsLife-Android-Direct-v{a}.apk.sha256",
        f"android-v{a}-manifest.json",f"android-signing-certificate-v{a}.txt",
        "AppBundle.zip","michels_life_icon.ico","release-provenance.json")
    return {
        "tag_name":f"v{w}-android-v{a}",
        "name":f"Michel's Life — Windows v{w} + Android v{a}",
        "draft":False,"prerelease":False,
        "assets":[{"name":n,"size":13,"digest":"sha256:"+hashlib.sha256(n.encode()).hexdigest()} for n in names]
    }


def data_pair(release):
    model=v.model(release)
    sha="a"*40
    p={"source_repo":v.SOURCE,"source_sha":sha,"source_run":45245978185,
       "publisher_run":45256957584,"windows_version":model["windows"],
       "android_version":model["android"],"android_version_code":model["code"],
       "android_certificate_sha256":v.CERT,
       "assets_sha256":{k:value for k,value in model["files"].items() if k!="release-provenance.json"}}
    m={"sourceSha":sha,"versionName":model["android"],"versionCode":model["code"],
       "signerCertSha256":v.CERT,"package":v.PKG,
       "platform":"android","distribution":"production-signed",
       "sha256":model["files"][f"MichelsLife-Android-Direct-v{model['android']}.apk"]}
    return model,p,m


class LatestStableVerifier(unittest.TestCase):
    def test_real_latest_and_next_adjacent_version_are_generated_dynamically(self):
        for win,android in [(231,20),(232,21),(233,22)]:
            m=v.model(fixture(win,android))
            self.assertEqual(m["code"],android+2)
            self.assertEqual(len(m["files"]),13)
            self.assertIn(f"MichelsLife-Android-Direct-v0.2.{android}.apk",m["files"])
            m,p,manifest=data_pair(fixture(win,android))
            self.assertEqual(v.metadata(fixture(win,android),m,p,manifest),
                             (45245978185,45256957584,"a"*40))

    def test_draft_prerelease_legacy_and_other_app_rejected(self):
        for key in ("draft","prerelease"):
            x=fixture()
            x[key]=True
            with self.assertRaises(ValueError):v.model(x)
        for win,android in [(217,5),(230,18),(232,20)]:
            with self.assertRaises(ValueError):v.model(fixture(win,android))
        x=fixture()
        x["tag_name"]="louderme-v3.0.231-android-v0.2.20"
        with self.assertRaises(ValueError):v.model(x)

    def test_malformed_asset_inventory_or_missing_digest_fails_closed(self):
        x=fixture();x["assets"].pop()
        with self.assertRaises(ValueError):v.model(x)
        x=fixture();x["assets"][1]["name"]=x["assets"][0]["name"]
        with self.assertRaises(ValueError):v.model(x)
        x=fixture();x["assets"][7]["digest"]=None
        with self.assertRaises(ValueError):v.model(x)

    def test_manifests_and_all_twelve_asset_hashes_are_required(self):
        rel=fixture()
        m,p,manifest=data_pair(rel)
        self.assertEqual(v.metadata(rel,m,p,manifest),(45245978185,45256957584,"a"*40))
        p["android_certificate_sha256"]="0"*64
        with self.assertRaisesRegex(ValueError,"version/signature"):
            v.metadata(rel,m,p,manifest)
        p["android_certificate_sha256"]=v.CERT
        manifest["sha256"]="0"*64
        with self.assertRaisesRegex(ValueError,"Android APK manifest"):
            v.metadata(rel,m,p,manifest)
        manifest["sha256"]=m["files"]["MichelsLife-Android-Direct-v0.2.20.apk"]
        p["assets_sha256"]["AppBundle.zip"]="0"*64
        with self.assertRaisesRegex(ValueError,"asset hash drift"):
            v.metadata(rel,m,p,manifest)

    def test_sha_sidecar_checks_file_bytes_and_exact_filename(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            name="MichelsLife-Setup-v3.0.231.exe"
            data=b"actual binary fixture"
            digest=hashlib.sha256(data).hexdigest()
            (root/name).write_bytes(data)
            side=f"{digest}  {name}\n".encode()
            (root/(name+".sha256")).write_bytes(side)
            expected={name:digest,name+".sha256":hashlib.sha256(side).hexdigest()}
            v.sidecar(root,name,expected)
            (root/name).write_bytes(b"tampered")
            with self.assertRaisesRegex(ValueError,"does not match"):
                v.sidecar(root,name,expected)

    def test_verifier_uses_fixed_real_signer_and_same_sha_run_jobs(self):
        source=(HERE/"verify_latest_life_release.py").read_text()
        for term in [v.CERT,"signed-native-android15","source_run",
                     "publisher_run","releases/latest","apksigner",
                     "assets_sha256","GATES","sha256"]:
            self.assertIn(term,source)
        self.assertNotIn("TAG: v3.0.217",source)
        self.assertNotIn("05ccaa52c2899ba969d2d0ad396669d2552b0f2f",source)


if __name__=="__main__":
    unittest.main()
