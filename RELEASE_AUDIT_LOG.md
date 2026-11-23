# Michel's Life — Release Channel Audit Log

## 2026-11-23 — Post-publication verification tools repaired and independently green

- **Release actual permanece intacta:** [3.0.231 / Android0.2.20, 13 assets](https://github.com/michels-lab/michel-s-life-releases/releases/tag/v3.0.231-android-v0.2.20), última pública desde 2026-11-23 20:13:17 UTC. Publicador original #45256957584 SUCCESS.
- **Auditor de File Steward reparado:** fallo histórico #45256957609 por rebase concurrente de markdown/JSON reportes; [PR #22](https://github.com/michels-lab/michel-s-life-releases/pull/22) MERGED; [primer auditor real main #45262231059](https://github.com/michels-lab/michel-s-life-releases/actions/runs/45262231059) SUCCESS. Se probaron dos clones que escriben al mismo tiempo, rechazo de push y no-force; generación desde `origin/main` actualizado, solo cuatro archivos permitidos.
- **Verificador público latest reparado:** viejo [run #45262323163](https://github.com/michels-lab/michel-s-life-releases/actions/runs/45262323163) falló porque exigía históricamente v3.0.217/Android0.2.5 y SHAs/runs caducados. [PR #23](https://github.com/michels-lab/michel-s-life-releases/pull/23) MERGED; [**verificación live main #45263145707**](https://github.com/michels-lab/michel-s-life-releases/actions/runs/45263145707) **SUCCESS**. La comprobación lee la release latest real, exige 13 assets/nombres/hashes exactos, descarga 3 binarios actuales (Setup, Portable, Android Direct), compara SHA256 de archivos y sidecars, verifica la firma permanente Android con `apksigner`, paquete/código con `aapt`, manifiesto y procedencia 12/13, consulta source y publisher runs exitosos, y las nueve suites del SHA exacto. El flujo no declara QA física ni finge corregir sus rojos históricos.
- **Aceptación pendiente:** owner escucha Mozart/Chaikovski en Windows/Galaxy físico; son fragmentos sintetizados, NO composiciones completas. Alarma real bajo Doze y MP3, datos privados en upgrade, Supabase/OAuth, #168 y estética sin certificar, 7/15 = 47% de progreso integral.

---

## 2026-11-23 — Verificada la estable 3.0.231 / Android Direct 0.2.20

**ÚLTIMA release oficial** [v3.0.231-android-v0.2.20](https://github.com/michels-lab/michel-s-life-releases/releases/tag/v3.0.231-android-v0.2.20) publicada `2026-11-23T20:13:17Z`, `draft=false`, `prerelease=false`, **13 assets** con checksums. Source SHA exacto `9ce4881b93e16f378f7f78c1808c897d385d67fc`, [source run #45245978185](https://github.com/michels-lab/michel-s-life/actions/runs/45245978185) **SUCCESS** con 9/9 workflows de producto sobre mismo commit; jobs `exact-source`, Windows, Android firmado y `signed-native-android15` SUCCESS. [Destination publisher #45256957584](https://github.com/michels-lab/michel-s-life-releases/actions/runs/45256957584) **SUCCESS**, intent aislado `f6b6e65df6b5c037be590d498eee2bd1c609c51f`, verificación de certificado permanente, versionCode22, manifiesto/procedencia SHA, Windows Setup y Portable arrancados, checksums y 13 assets comprobados en descarga antes de publicar.

**Novedad principal:** botones **Mozart K.545** y **Chaikovski Op.39/1** visibles y seleccionables en Focus Windows/Android, selección persistente y controles de reproducción probados; **fragmentos sintetizados**, no obras o grabaciones completas. Anteriores ocho ambientaciones y siete sonidos de fin conservados.

**Verificación Android in-place independiente:** [CI #44860600222](https://github.com/michels-lab/michel-s-life/actions/runs/44860600222) SUCCESS 0.2.18→0.2.19 con firma/UID estable sin desinstalar; no inspecciona contenido privado de WebView y no prueba Galaxy físico. **Auditor File Steward de destino #45256957609 FAILED** concurrente al publicador por rebase de reportes; NO invalida release. Corrección con prueba real de dos clones Git y fail-closed integrada en [PR #22](https://github.com/michels-lab/michel-s-life-releases/pull/22) SHA `7be050098af36c757c68046d48e8509277b48cef`; no reescribir retroactivamente el fallo. Aceptación integral 7/15 (47%), no 100%.

---

## 2026-11-20 México / 2026-11-21 UTC — Verified stable Windows 3.0.230 + Android Direct 0.2.19 (Settings + classical Focus)

**Current latest public release:** [v3.0.230-android-v0.2.19](https://github.com/michels-lab/michel-s-life-releases/releases/tag/v3.0.230-android-v0.2.19) publicado **2026-11-21 00:31:09 UTC**, `draft=false`, `prerelease=false`, 13 assets. Release anterior 3.0.229/0.2.18 preservada sin sobrescribir.

**Fuente exacta y build:** `9e3a3abc84c811fc2baf4eb64e5a50ca1ccc31cf`; [source run #44842053581](https://github.com/michels-lab/michel-s-life/actions/runs/44842053581) **SUCCESS**, 9/9 gates de Source, Windows UI, Android UI, Direct updater, Quick Mission, Focus inmersivo, Personal Alarms, Settings color persistence y clásica SUCCESS sobre ese SHA; `exact-source`, `windows / build`, `android / android` y `signed-native-android15` SUCCESS. Windows Setup y Portable iniciados en CI; Android APK de producción Direct 0.2.19/code21 firmado usando certificado permanente y **realmente instalada/onboarded/reabierta** en Android15 emulado. Los tres artefactos fuente (Windows, Android Direct, test) y evidencia nativa están en #44842053581. No son pruebas de dispositivo físico.

**Publicador destino:** intent aislado commit `49f5a5ee61100d88dfb0a3c9e045ee1fc5173ea8`; [publisher #44844286557](https://github.com/michels-lab/michel-s-life-releases/actions/runs/44844286557) **SUCCESS**. Descargó Windows y APK producción del **mismo source run**, inspeccionó certificados Android, `versionCode21`, manifiesto y SHA, validó hashes de los tres ejecutables Windows e iniciación, construyó 13 assets, publicó primero un draft, verificó descargas/checksums/provenance y convirtió a `latest` solo después de satisfacer la inspección.

**Incluye:** PR [#225](https://github.com/michels-lab/michel-s-life/pull/225) Settings floating color preview y almacenamiento persistente empaquetado (Windows+WebView Android); PR [#226](https://github.com/michels-lab/michel-s-life/pull/226) miniaturas de motivos clásicos públicos Mozart K545 y Chaikovski Op39/1 sintetizadas en Web Audio, ocho ambientes previos preservados; #227 versionado exacto. Sin grabaciones comerciales o obras completas, RC ni Developer Edition.

**Limitaciones honestas:** el File Steward audit independiente source falló por conflicto `git push` de reporte mientras otro escritor actualizó main (no es uno de los nueve checks de release). Algunos emuladores Android14/16 debug de PR previos perdieron ADB/QEMU y no se declaran aprobados. No certificada prueba física Samsung bajo bloqueo/Doze, MP3 personal, upgrade in-place sin pérdida, cuentas reales Google/Supabase, error JS [#168](https://github.com/michels-lab/michel-s-life/issues/168) reparado o Microsoft/Google Store.



## 2026-11-19 — Verified stable Windows 3.0.229 + Android Direct 0.2.18 (cinematic alarms)

**Current latest public release:** [v3.0.229-android-v0.2.18](https://github.com/michels-lab/michel-s-life-releases/releases/tag/v3.0.229-android-v0.2.18), published 2026-11-19 07:18:56 UTC, `draft=false`, `prerelease=false`, 13 public assets. Prior 3.0.228/0.2.17 tag remains untouched.

**Source provenance:** exact source release-intent SHA `ac17aefe8b5357f36ae941920774dd652c9f4050`, source pipeline [#44476655063](https://github.com/michels-lab/michel-s-life/actions/runs/44476655063) **SUCCESS**; 7/7 mandatory UI, alarms, audio, source, Focus and Android updater checks GREEN. Windows Setup and Portable actually launched in native Windows CI; Android Direct v0.2.18 / code20 signed using pinned permanent certificate, manifest SHA-256 and same-source evidence, installed/onboarded/relaunched on Android15 AVD. Production signer pinned and checksum validated; separate dest intent `a715b3c34b47c0c5db5b984aa3a2baf3d3fae98a`; publisher [#44478564052](https://github.com/michels-lab/michel-s-life-releases/actions/runs/44478564052) **SUCCESS**, validated 13 distinct assets and published atomically.

**Included sound-design fixes:** six composed 24s original stereo alarm themes with evolving chords, bells, warm layers, echo and distinct pacing (source PR #221); Android v3 WAV cache and separate audible-fallback/silent-when-immersive notification channels; Windows no longer adds `SystemSounds.Exclamation` over an already-playing theme (PR #223). Original presets, custom audio and alarm scheduling retained; no third-party music samples.

**Limits:** Android emulator and source smoke are not physical-phone tests. Doze, locked device native sound choice, speaker aesthetic, in-place upgrade/persistence, OAuth/Supabase and intermittent source issue #168 remain unverified. No Play Store, Microsoft Store, RC or Developer Edition published. This log records a release already confirmed through GitHub API; it does not create or rewrite distribution assets.

## 2026-11-18 Mexico / 2026-11-19 UTC — Windows 3.0.228 + Android Direct 0.2.17: published and verified

**Current unified stable tag:** [v3.0.228-android-v0.2.17](https://github.com/michels-lab/michel-s-life-releases/releases/tag/v3.0.228-android-v0.2.17), published 2026-11-19 05:50:18 UTC, `draft=false`, `prerelease=false`, 13 public assets.

**Full provenance chain:** source SHA `0a9b6e966c25d9400a0e7db15c5f8aec1acb995a`, source Actions [#44466658753](https://github.com/michels-lab/michel-s-life/actions/runs/44466658753) **SUCCESS**, signed Android Direct 0.2.17 / code19 using the pinned permanent certificate, real Android15 emulated APK installation/onboarding/relaunch screenshots, Windows Setup + Portable real launch and SHA-256 checks. Separate one-file destination publishing intent `a84b9677ae4e02c5cb792f4394d77c50a15bac3d`; destination Actions [#44467820961](https://github.com/michels-lab/michel-s-life-releases/actions/runs/44467820961) **SUCCESS** verified source, exact same-run artifacts, SHA-256 sidecars, permanent certificate, provenance and 13 asset names before atomically publishing. Prior 3.0.227/0.2.16 tag remains unmodified.

**Scope / nonclaims:** No Windows/Android Developer Edition or RC. AVD-native success is not Samsung Galaxy physical certification (Doze, custom ringtone, lock-screen overlay), live OAuth/Supabase account verification, signed in-place upgrade preservation, or Android14/16 hosted ADB stability. Source issue [#168](https://github.com/michels-lab/michel-s-life/issues/168) remains open. This is a release audit record, not a second publication.

## 2026-10-20 — GRANADA ambition mandate registered (distribution only)

Owner order: GRANADA shall execute large, ambitious, cohesive, end-to-end blocks (typically 3–6 substantial independent work packages if safe and relevant), rather than serial one-line fixes. Source of truth: https://github.com/michels-lab/Michel-Software-Standards/blob/main/standards/OPERACION_GRANADA_STANDARD.md.

This is a release/distribution repository, so Granada work here means **read-only installation metadata, feed/checksum/link validation, evidence, documentation and handoffs**. No binary replacement, tag, version, installer publication, or user data modification without a separate explicit release order. This governance entry is documentation only; it does not claim any release was created or validated.

