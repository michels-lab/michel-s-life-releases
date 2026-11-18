# Michel's Life — Official Public Releases

This public repository is the official customer-facing binary/update channel exclusively for **Michel's Life**. Application source code and development history live in the separate app repository.

## Michel's Life — unified Windows + Android release

[Operación Granada — auditoría del repo de distribución y plugins](docs/GRANADA_DISTRIBUTION_PLUGIN_AUDIT_2026-10-21.md).

**Latest GitHub-published unified stable release (API verified 2026-11-18):** [v3.0.227-android-v0.2.16](https://github.com/michels-lab/michel-s-life-releases/releases/tag/v3.0.227-android-v0.2.16), published **2026-11-18 19:22:02 UTC**, **13 assets**, `draft=false`, `prerelease=false`. [Verified destination publisher run #44379633157](https://github.com/michels-lab/michel-s-life-releases/actions/runs/44379633157) **SUCCESS**; [source build/CI run #44377747872](https://github.com/michels-lab/michel-s-life/actions/runs/44377747872) **SUCCESS**, exactly `773dd064e4c54cd68ac464d60d55d2d957b73e36`.

- **Windows v3.0.227:** Setup and Portable executable plus legacy updater alias, matching SHA-256 sidecars, validated installed/portable launch.
- **Android Direct v0.2.16 (versionCode 18):** signed with the existing permanent Direct certificate, pinned SHA-256, verified native install/onboarding/relaunch with actual screenshots on Android 15 emulator. This is not a Google Play release.
- **What's fixed:** old Focus dock/sidebar UI removed from source (not CSS-hidden); immersive Pomodoro legible with official wallpaper and affirmations beneath controls, original 24-second six-tone alarm suite including Radar, personal ringtone import and recurring/quick alarms; Windows native Focus notifications.
- **Evidence and limits:** same-SHA source/UI/updater tests, Windows installed launch, signed native Android15 relaunch, certificate and digest verification, and **13 downloaded/public assets**. Physical Samsung lock-screen/Doze/MP3, in-place user-data retention, live OAuth/Supabase, and intermittent JavaScript [#168](https://github.com/michels-lab/michel-s-life/issues/168) remain separate acceptance tasks. Previous 3.0.226/0.2.15 remains historical; no RC or Developer Edition.

**Android upgrade precautions:** the earlier v0.2.2 TEST APK had a different debug certificate; a direct upgrade across signing identities is unsupported. Back up existing data before reinstalling. Device-specific retention and same-account synchronization remain separate acceptance tests.

Every Michel's Lab product must publish one unified public release per app with all currently distributed platforms. Michel's Life Desktop's direct updater consults this public repository and checks release hashes. Keep LouderMe releases exclusively in [LouderME-Releases](https://github.com/michels-lab/LouderME-Releases/releases).

## Compatibility for old installed LouderMe clients (not releases)

**No LouderMe releases or installers are published in this repository.** All LouderMe release history and new Android/Windows unified releases belong exclusively to [LouderME-Releases](https://github.com/michels-lab/LouderME-Releases/releases).

On 2026-10-11, after verifying all **13** original LouderMe release copies in the product-only repository against their original binary sizes and SHA-256 digests, the 13 LouderMe releases and old release tags were deleted from this Michel's Life repository. The old manually pinned `/releases/download/louderme-*/...` URLs no longer work; use the LouderMe-only release URLs instead.

Only two legacy, **non-release** update manifests remain (`louderme/latest.json`, `louderme-desktop/latest.json`). Existing installed LouderMe versions contain hardcoded URLs to those manifest paths, so they are kept strictly as redirects-through-metadata to the new LouderMe-only binary downloads. They do not contain installers and cannot create LouderMe releases here. Once older clients no longer need these two files, they can be retired.

## Security

Public availability of a binary does not make the proprietary application source open source.

Clients must never require a private GitHub token to check for or download an update.
