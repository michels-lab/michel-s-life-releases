# Michel's Lab — Public Release Channels

This public repository distributes installable binaries and update feeds for selected **Michel's Lab** applications. Application source code and development history live in their own repositories.

## Michel's Life — unified Windows + Android release

**One public release page per product, with current Windows and Android binaries together:** https://github.com/michels-lab/michel-s-life-releases/releases/tag/v3.0.216

- **Windows v3.0.216:** `MichelsLife-Setup-v3.0.216.exe` is the recommended installer; `MichelsLife-Portable-v3.0.216.exe` is optional; `MichelsLife-v3.0.216.exe` is a byte-identical legacy updater alias. Each executable has its SHA-256 sidecar.
- **Android Direct v0.2.3, versionCode 5:** `MichelsLife-Android-Direct-v0.2.3.apk` is the permanently owner-signed direct installer with SHA-256 and signing/provenance metadata, on the SAME `v3.0.216` release.
- `AppBundle.zip` and `michels_life_icon.ico` remain internal/branding assets for the Windows bootstrap.

**Android upgrade warning:** The older v0.2.2 TEST APK was signed with a temporary debug certificate. The current **permanently signed** Direct v0.2.3 APK may **not** update that TEST installation in place; export/back up existing app data and verify recoverability before any uninstall/reinstall. Keep the current Direct signing key for all future direct updates. Google Play and Microsoft Store publication are separate from this direct GitHub release.

For EVERY multi-platform Michel's Lab app the public binary release must include all shipped platforms together, with real independent platform version numbers. When just one platform changes, carry forward the other platform's verified current assets. CI artifacts and separate store submissions are not substitute public releases.

Michel's Life direct-updater Windows checks this public repository for newer official releases and verifies published checksums before applying direct updates. Google Play and Microsoft Store are separate provider-managed channels.


## LouderMe — unified Android + Windows releases

LouderMe source remains private. Its public GitHub release surface is unified: the current stable Android and Windows binaries live together on one LouderMe release page.

A unified release can contain:
- `LouderMe-vA.B.C-sideload.apk` — Michel's Lab Direct Android build;
- `LouderMe-Setup-vX.Y.Z.exe` — recommended Windows installer;
- `LouderMe-Portable-vX.Y.Z.exe` — optional Windows portable build;
- matching SHA-256 checksum files for every binary.

Android and Windows may keep different real platform versions. The unified release title/tag identifies both versions instead of pretending they are equal.

Platform-specific updater manifests remain separate:
- `louderme/latest.json` — Android direct/sideload feed;
- `louderme-desktop/latest.json` — Windows stable feed.

Both manifests point into the same unified public release. When only one platform changes, the publisher carries forward the current validated artifacts of the unchanged platform.

Google Play builds still use Google Play's update channel. Windows Authenticode signing is not yet configured for LouderMe Desktop, so SmartScreen can still warn for an unsigned/new publisher binary.

## Security

Public availability of a binary does not make the proprietary application source open source.

Clients must never require a private GitHub token to check for or download an update.
