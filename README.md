# Michel's Life — Official Public Releases

This public repository is the official customer-facing binary/update channel exclusively for **Michel's Life**. Application source code and development history live in the separate app repository.

## Michel's Life — unified Windows + Android release

**One public release page per product, with current Windows and Android binaries together:** https://github.com/michels-lab/michel-s-life-releases/releases/tag/v3.0.216

- **Windows v3.0.216:** `MichelsLife-Setup-v3.0.216.exe` is the recommended installer; `MichelsLife-Portable-v3.0.216.exe` is optional; `MichelsLife-v3.0.216.exe` is a byte-identical legacy updater alias. Each executable has its SHA-256 sidecar.
- **Android Direct v0.2.4, versionCode 6:** `MichelsLife-Android-Direct-v0.2.4.apk` is the current permanently owner-signed direct installer with SHA-256 and signing/provenance metadata, on the SAME `v3.0.216` release. Android v0.2.4 adds phone-specific navigation, Focus, Quick Capture, compact Dashboard, Settings and Missions/Calendar/Journal layouts.
- `AppBundle.zip` and `michels_life_icon.ico` remain internal/branding assets for the Windows bootstrap.

**Android upgrade warning:** The old v0.2.2 TEST APK was signed with a temporary debug certificate; it cannot be updated directly using the permanent Direct key. Export/back up your app data and verify recovery before uninstalling a TEST build. Android Direct v0.2.4 uses the **same permanent signing key** as v0.2.3 and increases versionCode to 6, so normal in-place updates from v0.2.3 should preserve local data; back up first. Google Play and Microsoft Store publication are separate from this direct GitHub release. Native background alarms, physical Galaxy UI acceptance and live Windows↔Galaxy Supabase account sync are still unverified.

For EVERY multi-platform Michel's Lab app the public binary release must include all shipped platforms together, with real independent platform version numbers. When just one platform changes, carry forward the other platform's verified current assets. CI artifacts and separate store submissions are not substitute public releases.

Michel's Life direct-updater Windows checks this public repository for newer official releases and verifies published checksums before applying direct updates. Google Play and Microsoft Store are separate provider-managed channels.


## Compatibility for old installed LouderMe clients (not releases)

**No LouderMe releases or installers are published in this repository.** All LouderMe release history and new Android/Windows unified releases belong exclusively to [LouderME-Releases](https://github.com/michels-lab/LouderME-Releases/releases).

On 2026-10-11, after verifying all **13** original LouderMe release copies in the product-only repository against their original binary sizes and SHA-256 digests, the 13 LouderMe releases and old release tags were deleted from this Michel's Life repository. The old manually pinned `/releases/download/louderme-*/...` URLs no longer work; use the LouderMe-only release URLs instead.

Only two legacy, **non-release** update manifests remain (`louderme/latest.json`, `louderme-desktop/latest.json`). Existing installed LouderMe versions contain hardcoded URLs to those manifest paths, so they are kept strictly as redirects-through-metadata to the new LouderMe-only binary downloads. They do not contain installers and cannot create LouderMe releases here. Once older clients no longer need these two files, they can be retired.

## Security

Public availability of a binary does not make the proprietary application source open source.

Clients must never require a private GitHub token to check for or download an update.
