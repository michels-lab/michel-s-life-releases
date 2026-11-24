"""Static fail-closed checks for staged Michel's Life 3.0.232/0.2.21 publisher.
These source assertions do not replace actual signed APK, Windows binary or GitHub
release validation; the deployment workflow must still obtain all artifacts.
"""
from pathlib import Path
import re
import unittest

WORKFLOW = Path(".github/workflows/publish-life-v3232-a0221-destination.yml")
RELEASE_INTENT = ".michelslab/release-intents/life-v3232-a0221-destination.txt"
CHECKS = (
    "Source validation",
    "UI smoke",
    "Android UI smoke",
    "GRANADA Settings live color persistence",
    "GRANADA classical Focus excerpts",
    "GRANADA - Story Focus touch provenance",
    "GRANADA Data Health and recovery safety",
)
ASSETS = (
    "MichelsLife-Setup-v3.0.232.exe",
    "MichelsLife-Setup-v3.0.232.exe.sha256",
    "MichelsLife-Portable-v3.0.232.exe",
    "MichelsLife-Portable-v3.0.232.exe.sha256",
    "MichelsLife-v3.0.232.exe",
    "MichelsLife-v3.0.232.exe.sha256",
    "MichelsLife-Android-Direct-v0.2.21.apk",
    "MichelsLife-Android-Direct-v0.2.21.apk.sha256",
    "android-v0.2.21-manifest.json",
    "android-signing-certificate-v0.2.21.txt",
    "AppBundle.zip",
    "michels_life_icon.ico",
    "release-provenance.json",
)


class PublisherConfig(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = WORKFLOW.read_text(encoding="utf8")

    def test_frozen_versions_and_source_sha_intent(self):
        s = self.source
        self.assertIn("TAG: v3.0.232-android-v0.2.21", s)
        self.assertIn(RELEASE_INTENT, s)
        self.assertIn('test "$(git diff --name-only HEAD^ HEAD)"', s)
        self.assertIn("SOURCE_RUN: ''", s)
        self.assertIn("SOURCE_SHA: ''", s)
        self.assertIn("SOURCE_RUN=\"$(jq -er", s)
        self.assertIn("SOURCE_SHA=\"$(jq -er", s)
        self.assertNotIn("v3.0.229", s)
        self.assertNotIn("v0.2.18", s)

    def test_real_source_checks_and_signed_native_provenance(self):
        s = self.source
        for name in CHECKS:
            self.assertIn('"'+name+'"', s)
        for marker in (
            "source-run.json", "sha-runs.json", "source-jobs.json",
            "exact-source", "windows / build", "android / android",
            "signed-native-android15",
            ".sourceSha==$sha", ".signerCertSha256==$cert",
            '.versionName=="0.2.21"', '.versionCode==23',
            "apksigner", "aapt", "ANDROID_CERT_PIN",
            "sha256sum -c", "LAUNCH PASS",
        ):
            self.assertIn(marker, s)
        self.assertRegex(s, r"android_version_code[\"']?:23")
        self.assertNotIn("continue-on-error", s)
        self.assertNotIn("|| true", s)

    def test_exact_thirteen_assets_and_only_atomic_draft_publication(self):
        s = self.source
        self.assertEqual(len(ASSETS), 13)
        for name in ASSETS:
            self.assertIn(name, s)
        for marker in (
            "gh release create", "--draft", "(.assets|length)==13",
            "sha256sum -c", "gh release download", "cmp -s",
            "--draft=false --latest", "releases/latest", "release-provenance.json",
        ):
            self.assertIn(marker, s)
        idx_create = s.index("gh release create")
        idx_verify = s.index("(.assets|length)==13")
        idx_public = s.index("--draft=false --latest")
        self.assertLess(idx_create, idx_verify)
        self.assertLess(idx_verify, idx_public)


if __name__ == "__main__":
    unittest.main()
