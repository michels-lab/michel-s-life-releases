#!/usr/bin/env python3
"""Audit the actual latest unified Michel's Life stable, never a frozen old tag.

Uses GitHub's newest public release, live source/publisher provenance, physical
SHA256 of downloaded setup/portable/APK, Android's SDK signature and package
tools. A pinned permanent owner certificate is intentionally NOT dynamic.
"""
from __future__ import annotations
import argparse,hashlib,json,os,re,subprocess
from pathlib import Path

REPO="michels-lab/michel-s-life-releases"
SOURCE="michels-lab/michel-s-life"
CERT="36a9f5144243d14ebade9d38559cfd7d4d9207c1edba01e6f0fbdd5f076a50fa"
PKG="com.michelslab.michelslife"
TAGS=re.compile(r"^v3\.0\.(\d+)-android-v0\.2\.(\d+)$")
HEX40=re.compile(r"^[0-9a-f]{40}$")
HEX64=re.compile(r"^[0-9a-f]{64}$")
GATES=(
    "Source validation","UI smoke","Android UI smoke",
    "GRANADA Android Direct safe update discovery",
    "GRANADA Quick Mission and original Pomodoro audio",
    "GRANADA cross-platform immersive Focus",
    "GRANADA personal alarms — Windows and Android contracts",
    "GRANADA Settings live color persistence",
    "GRANADA classical Focus excerpts")
JOBS=("exact-source","windows / build","android / android","signed-native-android15")


def cmd(*args, quiet=False):
    p=subprocess.run(list(args),check=True,text=True,
        stdout=subprocess.DEVNULL if quiet else subprocess.PIPE)
    return "" if quiet else p.stdout


def api(endpoint):
    return json.loads(cmd("gh","api",endpoint))


def model(latest):
    if latest.get("draft") is not False or latest.get("prerelease") is not False:
        raise ValueError("latest release must be published stable, not draft/RC")
    match=TAGS.fullmatch(str(latest.get("tag_name","")))
    if not match:
        raise ValueError("latest tag must be an official unified product tag")
    windows,android=map(int,match.groups())
    if windows<230 or android<19 or windows-android!=211:
        raise ValueError("version pairing does not match canonical release sequence")
    w,v=f"3.0.{windows}",f"0.2.{android}"
    title=latest.get("name") or ""
    if f"Windows v{w}" not in title or f"Android v{v}" not in title:
        raise ValueError("latest title mismatches unified tag")
    expected=(
      f"MichelsLife-Setup-v{w}.exe",f"MichelsLife-Setup-v{w}.exe.sha256",
      f"MichelsLife-Portable-v{w}.exe",f"MichelsLife-Portable-v{w}.exe.sha256",
      f"MichelsLife-v{w}.exe",f"MichelsLife-v{w}.exe.sha256",
      f"MichelsLife-Android-Direct-v{v}.apk",
      f"MichelsLife-Android-Direct-v{v}.apk.sha256",
      f"android-v{v}-manifest.json",f"android-signing-certificate-v{v}.txt",
      "AppBundle.zip","michels_life_icon.ico","release-provenance.json")
    assets=latest.get("assets")
    if not isinstance(assets,list) or len(assets)!=13:
        raise ValueError("expected exactly 13 official public files")
    names=[a["name"] for a in assets]
    if len(set(names))!=13 or set(names)!=set(expected):
        raise ValueError("official 13-file inventory mismatches current versions")
    for a in assets:
        digest=a.get("digest") or ""
        if not isinstance(a.get("size"),int) or a["size"]<=0 or not digest.startswith("sha256:") or not HEX64.fullmatch(digest[7:]):
            raise ValueError("missing asset size or GitHub sha256 digest")
    return dict(tag=latest["tag_name"],windows=w,android=v,code=android+2,
                files={a["name"]:a["digest"][7:] for a in assets})


def metadata(latest,m,provenance,manifest):
    sha=provenance.get("source_sha")
    run=provenance.get("source_run")
    publish=provenance.get("publisher_run")
    if provenance.get("source_repo")!=SOURCE or not isinstance(sha,str) or not HEX40.fullmatch(sha):
        raise ValueError("untrusted source provenance")
    if any(type(x) is not int or x<=0 for x in (run,publish)):
        raise ValueError("source/publisher workflow ids missing")
    if (provenance.get("windows_version")!=m["windows"] or
        provenance.get("android_version")!=m["android"] or
        provenance.get("android_version_code")!=m["code"] or
        provenance.get("android_certificate_sha256")!=CERT):
        raise ValueError("version/signature provenance differs from latest")
    hashes=provenance.get("assets_sha256")
    if not isinstance(hashes,dict) or len(hashes)!=12:
        raise ValueError("provenance must pin all 12 original public assets")
    for name,digest in m["files"].items():
        if name!="release-provenance.json" and hashes.get(name)!=digest:
            raise ValueError("release asset hash drift: "+name)
    if (manifest.get("sourceSha")!=sha or
        manifest.get("versionName")!=m["android"] or
        manifest.get("versionCode")!=m["code"] or
        manifest.get("signerCertSha256")!=CERT or
        manifest.get("package")!=PKG or
        manifest.get("distribution")!="production-signed" or
        manifest.get("platform")!="android" or
        manifest.get("sha256")!=m["files"][f"MichelsLife-Android-Direct-v{m['android']}.apk"]):
        raise ValueError("Android APK manifest/source/signer mismatch")
    return run,publish,sha


def real_runs(source_run,publisher_run,sha):
    src=api(f"repos/{SOURCE}/actions/runs/{source_run}")
    pub=api(f"repos/{REPO}/actions/runs/{publisher_run}")
    if src.get("head_sha")!=sha or src.get("conclusion")!="success" or src.get("event")!="push":
        raise ValueError("source run is not same SHA, completed and green")
    if pub.get("conclusion")!="success" or pub.get("event")!="push":
        raise ValueError("publisher run did not succeed")
    jobs=api(f"repos/{SOURCE}/actions/runs/{source_run}/jobs?per_page=100")["jobs"]
    for job in JOBS:
        if not any(x.get("name")==job and x.get("conclusion")=="success" for x in jobs):
            raise ValueError("exact source native/build job not green: "+job)
    checks=api(f"repos/{SOURCE}/actions/runs?head_sha={sha}&per_page=100")["workflow_runs"]
    for gate in GATES:
        if not any(x.get("name")==gate and x.get("head_sha")==sha and x.get("conclusion")=="success" for x in checks):
            raise ValueError("source SHA product gate not green: "+gate)


def hash_file(path):
    h=hashlib.sha256()
    with path.open("rb") as handle:
        while chunk:=handle.read(1024*1024):
            h.update(chunk)
    return h.hexdigest()


def sidecar(directory,name,expected):
    text=(directory/(name+".sha256")).read_text(encoding="utf-8").split()
    if len(text)!=2 or text[1].lstrip("*")!=name or not HEX64.fullmatch(text[0]):
        raise ValueError("sidecar invalid or does not bind downloaded binary")
    if hash_file(directory/name)!=text[0] or text[0]!=expected[name]:
        raise ValueError("downloaded executable/APK does not match public SHA: "+name)
    if hash_file(directory/(name+".sha256"))!=expected[name+".sha256"]:
        raise ValueError("checksum sidecar changed on GitHub")


def verify(repo,directory):
    if repo!=REPO: raise ValueError("refuse foreign release repository")
    latest=api(f"repos/{REPO}/releases/latest")
    m=model(latest)
    directory.mkdir(parents=True,exist_ok=True)
    binaries=(
      f"MichelsLife-Setup-v{m['windows']}.exe",
      f"MichelsLife-Portable-v{m['windows']}.exe",
      f"MichelsLife-Android-Direct-v{m['android']}.apk")
    download=[*binaries,*(name+".sha256" for name in binaries),
              f"android-v{m['android']}-manifest.json","release-provenance.json"]
    args=["gh","release","download",m["tag"],"--repo",REPO,"--dir",str(directory)]
    for name in download:args.extend(["--pattern",name])
    cmd(*args,quiet=True)
    for name in download:
        path=directory/name
        if not path.is_file() or not path.stat().st_size or hash_file(path)!=m["files"][name]:
            raise ValueError("missing/corrupted public download: "+name)
    for binary in binaries:sidecar(directory,binary,m["files"])
    manifest=json.loads((directory/f"android-v{m['android']}-manifest.json").read_text())
    provenance=json.loads((directory/"release-provenance.json").read_text())
    source_run,publisher_run,sha=metadata(latest,m,provenance,manifest)
    real_runs(source_run,publisher_run,sha)
    sdk=Path(os.environ["ANDROID_HOME"])/"build-tools"/"36.0.0"
    apk=directory/binaries[2]
    sig=cmd(str(sdk/"apksigner"),"verify","--verbose","--print-certs",str(apk))
    cert=re.search(r"Signer #1 certificate SHA-256 digest:\s*([0-9a-fA-F:]+)",sig)
    if cert is None or cert.group(1).replace(":","").lower()!=CERT:
        raise ValueError("downloaded production APK signer is NOT owner-pinned certificate")
    badging=cmd(str(sdk/"aapt"),"dump","badging",str(apk))
    for part in (f"name='{PKG}'",f"versionCode='{m['code']}'",f"versionName='{m['android']}'"):
        if part not in badging:raise ValueError("installed APK badging does not match: "+part)
    print(f"VERIFIED_LATEST_PUBLIC_STABLE: {m['tag']} 13 assets, source run {source_run} and publisher run {publisher_run} SUCCESS; nine exact-SHA gates, four native/build jobs, three real binary checksums, pinned production Android signer. Physical owner acceptance NOT implied.")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--repo",default=REPO)
    p.add_argument("--directory",type=Path,default=Path("artifacts/verified-latest"))
    a=p.parse_args()
    verify(a.repo,a.directory)
