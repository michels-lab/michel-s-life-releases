# Michel's Life — Official Public Releases

This public repository is the official customer-facing binary/update channel exclusively for **Michel's Life**. Application source code and development history live in the separate app repository.

## Michel's Life — unified Windows + Android release

[Operación Granada — auditoría del repo de distribución y plugins](docs/GRANADA_DISTRIBUTION_PLUGIN_AUDIT_2026-10-21.md).

**Latest GitHub-published unified release (API verified 2026-10-21):** [v3.0.221](https://github.com/michels-lab/michel-s-life-releases/releases/tag/v3.0.221), published 2026-10-19.

- **Windows v3.0.221:** Setup, Portable and compatibility alias with SHA-256 sidecars.
- **Android Direct v0.2.9:** signed-channel APK, SHA-256 sidecar and signing-certificate description; version is separate from the Windows version.
- The release also contains `AppBundle.zip`, official icon, Android manifest and source `release-provenance.json`; GitHub release inventory returned **13 assets**.
- **Scope of verification:** asset metadata/tag via GitHub API, not local executable, native reinstall, source-SHA reproducibility, live Samsung data persistence or two-device synchronization. [App source/CI audit](https://github.com/michels-lab/michel-s-life/blob/main/docs/GRANADA_APP_PLUGIN_AUDIT_2026-10-21.md).

**Android upgrade precautions:** the earlier v0.2.2 TEST APK had a different debug certificate; a direct upgrade across signing identities is unsupported. Back up existing data before reinstalling. Device-specific retention and same-account synchronization remain separate acceptance tests.

Every Michel's Lab product must publish one unified public release per app with all currently distributed platforms. Michel's Life Desktop's direct updater consults this public repository and checks release hashes. Keep LouderMe releases exclusively in [LouderME-Releases](https://github.com/michels-lab/LouderME-Releases/releases).

## Compatibility for old installed LouderMe clients (not releases)

**No LouderMe releases or installers are published in this repository.** All LouderMe release history and new Android/Windows unified releases belong exclusively to [LouderME-Releases](https://github.com/michels-lab/LouderME-Releases/releases).

On 2026-10-11, after verifying all **13** original LouderMe release copies in the product-only repository against their original binary sizes and SHA-256 digests, the 13 LouderMe releases and old release tags were deleted from this Michel's Life repository. The old manually pinned `/releases/download/louderme-*/...` URLs no longer work; use the LouderMe-only release URLs instead.

Only two legacy, **non-release** update manifests remain (`louderme/latest.json`, `louderme-desktop/latest.json`). Existing installed LouderMe versions contain hardcoded URLs to those manifest paths, so they are kept strictly as redirects-through-metadata to the new LouderMe-only binary downloads. They do not contain installers and cannot create LouderMe releases here. Once older clients no longer need these two files, they can be retired.

## Security

Public availability of a binary does not make the proprietary application source open source.

Clients must never require a private GitHub token to check for or download an update.
