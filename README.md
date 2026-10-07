# Michel's Lab — Public Release Channels

This public repository distributes installable binaries and update feeds for selected **Michel's Lab** applications. Application source code and development history live in their own repositories.

## Michel's Life — Windows

Official Windows distribution channel for **Michel's Life**, an RPG-inspired productivity and life-management desktop app.

Normal releases can include:

- `MichelsLife-Setup-vX.Y.Z.exe` — recommended Windows installer
- `MichelsLife-vX.Y.Z.exe` — portable build
- `MichelsLife-vX.Y.Z.exe.sha256` — SHA-256 checksum
- `AppBundle.zip` — internal bootstrap bundle
- `michels_life_icon.ico`

Michel's Life checks this public repository for newer official releases and verifies published checksums before applying direct updates.

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
