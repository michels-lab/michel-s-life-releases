# Michel's Life — Official Public Releases

This public repository is the official customer-facing binary/update channel exclusively for **Michel's Life**. Application source code and development history live in the separate app repository.

## Actual última estable verificada — Windows 3.0.230 + Android Direct 0.2.19

**[Descargar la release oficial unificada](https://github.com/michels-lab/michel-s-life-releases/releases/tag/v3.0.230-android-v0.2.19)**. Publicada **2026-11-21 00:31:09 UTC**, `draft=false`, `prerelease=false`, **13 archivos oficiales**. Última estable `v3.0.230-android-v0.2.19` confirmada en GitHub Releases API.

- **Windows 3.0.230:** Setup, Portable, alias ejecutable, tres checksums SHA-256, `AppBundle.zip` y icono. Instalada e iniciada en CI nativa de Windows.
- **Android Direct 0.2.19 (versionCode21):** APK de **producción** con certificado Direct permanente y verificado, SHA-256 y manifiesto de procedencia; se instaló, completó onboarding y relanzó en Android15 emulado desde el **mismo source run**. No es versión Play Store.
- **Incluye:** Settings con panel flotante contextual/live preview y persistencia de colores realmente empaquetado en Windows y Android ([PR #225](https://github.com/michels-lab/michel-s-life/pull/225)); fragmentos breves sintetizados de Mozart K545 y Chaikovski Op39/1 como dos temas de concentración adicionales, conservando ocho originales ([PR #226](https://github.com/michels-lab/michel-s-life/pull/226)). No son ejecuciones completas de piezas clásicas.
- **Evidencia exacta:** fuente `9e3a3abc84c811fc2baf4eb64e5a50ca1ccc31cf`, [CI source #44842053581](https://github.com/michels-lab/michel-s-life/actions/runs/44842053581) **SUCCESS** (nueve checks de producto + Windows + Android firmado/native), destino intent `49f5a5ee61100d88dfb0a3c9e045ee1fc5173ea8`, [publisher #44844286557](https://github.com/michels-lab/michel-s-life-releases/actions/runs/44844286557) **SUCCESS**. El publicador validó firma, manifiesto, hashes, 13 nombres/archivos y descarga comparada antes de marcar `latest`.
- **Límites de aceptación:** el audit File Steward de origen tuvo un conflicto de escritura concurrente separado de los nueve gates; Android14/16 debug hospedado de una prueba anterior perdió ADB/QEMU. No acreditamos prueba física Galaxy bajo bloqueo/Doze, MP3 en dispositivo real, actualización Direct in-place con datos del usuario, OAuth/Supabase reales, issue [#168](https://github.com/michels-lab/michel-s-life/issues/168) cerrado ni publicación Store. Sin RC/Developer Edition.

**Versión anterior:** [3.0.229 / 0.2.18](https://github.com/michels-lab/michel-s-life-releases/releases/tag/v3.0.229-android-v0.2.18), preservada íntegra.

---

## Historial: releases anteriores

[Operación Granada — auditoría del repo de distribución y plugins](docs/GRANADA_DISTRIBUTION_PLUGIN_AUDIT_2026-10-21.md).

**Historical GitHub-published unified stable release (API verified 2026-11-18):** [v3.0.227-android-v0.2.16](https://github.com/michels-lab/michel-s-life-releases/releases/tag/v3.0.227-android-v0.2.16), published **2026-11-18 19:22:02 UTC**, **13 assets**, `draft=false`, `prerelease=false`. [Verified destination publisher run #44379633157](https://github.com/michels-lab/michel-s-life-releases/actions/runs/44379633157) **SUCCESS**; [source build/CI run #44377747872](https://github.com/michels-lab/michel-s-life/actions/runs/44377747872) **SUCCESS**, exactly `773dd064e4c54cd68ac464d60d55d2d957b73e36`.

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
