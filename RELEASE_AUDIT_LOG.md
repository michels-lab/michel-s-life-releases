# Michel's Life — Release Channel Audit Log

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

