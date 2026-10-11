# Michel's Life — Official Public Releases

This public repository is the official customer-facing binary/update channel exclusively for **Michel's Life**. Application source code and development history live in the separate app repository.

## Michel's Life — unified Windows + Android release

**Current verified release:** https://github.com/michels-lab/michel-s-life-releases/releases/tag/v3.0.217

- **Windows v3.0.217:** recommended `MichelsLife-Setup-v3.0.217.exe`, optional `MichelsLife-Portable-v3.0.217.exe`, and byte-identical `MichelsLife-v3.0.217.exe` compatibility alias; individual SHA-256 companion files.
- **Android Direct v0.2.5 (versionCode 7):** `MichelsLife-Android-Direct-v0.2.5.apk` using the existing permanent signing certificate. Adds the full touch-oriented Missions editor with weekly recurrence and sticky Save/Cancel while preserving the shared canonical mission data.
- `AppBundle.zip`, official icon, Android signing certificate, manifest and `release-provenance.json` accompany these actual binaries.
- **Validation:** exact-source CI, Windows Setup install + executable launch, Android Direct signer/package/hash checks, native Android 16 install/relaunch with screenshots, and destination-owned draft verification completed successfully. [Publishing evidence](https://github.com/michels-lab/michel-s-life-releases/actions/runs/38176304417).

**Android upgrade precautions:** Old v0.2.2 TEST APKs used a different debug certificate and cannot update in place. Export or back up data before switching from the TEST build. Direct v0.2.5 uses the same permanent Direct signer as v0.2.4 and increases versionCode from 6 to 7. Normal installation over an existing compatible Direct installation should be possible, but actual Samsung Galaxy data-retention testing is still pending. Store publication and real Windows↔Galaxy Supabase/Google sync are separate and not implied.

Every Michel's Lab product must publish one unified public release per app with all currently distributed platforms. Michel's Life Desktop's direct updater consults this public repository and checks release hashes. Keep LouderMe releases exclusively in [LouderME-Releases](https://github.com/michels-lab/LouderME-Releases/releases).

## Compatibility for old installed LouderMe clients (not releases)

**No LouderMe releases or installers are published in this repository.** All LouderMe release history and new Android/Windows unified releases belong exclusively to [LouderME-Releases](https://github.com/michels-lab/LouderME-Releases/releases).

On 2026-10-11, after verifying all **13** original LouderMe release copies in the product-only repository against their original binary sizes and SHA-256 digests, the 13 LouderMe releases and old release tags were deleted from this Michel's Life repository. The old manually pinned `/releases/download/louderme-*/...` URLs no longer work; use the LouderMe-only release URLs instead.

Only two legacy, **non-release** update manifests remain (`louderme/latest.json`, `louderme-desktop/latest.json`). Existing installed LouderMe versions contain hardcoded URLs to those manifest paths, so they are kept strictly as redirects-through-metadata to the new LouderMe-only binary downloads. They do not contain installers and cannot create LouderMe releases here. Once older clients no longer need these two files, they can be retired.

## Security

Public availability of a binary does not make the proprietary application source open source.

Clients must never require a private GitHub token to check for or download an update.
