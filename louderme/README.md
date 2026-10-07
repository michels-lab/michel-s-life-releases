# LouderMe direct update feed

Public bootstrap/update feed for the **Michel's Lab** sideload build of LouderMe.

The source code remains in the private `realmichelduarte/LouderMe` repository.

## Contract

`latest.json` contains:
- package ID;
- versionCode/versionName;
- public APK URL;
- SHA-256 checksum;
- short release notes.

LouderMe additionally verifies the downloaded APK's:
- SHA-256;
- package ID;
- version code;
- Android signing certificate against the currently installed LouderMe sideload build.

Android still requires system/user approval to install an APK update.

## Signing

The direct channel must use one stable private signing key across releases. The signing key is never stored in this public repository.


## Unified public release surface

The Android updater manifest remains platform-specific, but its APK URL points into the same public GitHub release that also contains the current Windows Setup/Portable binaries and checksums.

Unified release titles identify both real platform versions when they differ.
