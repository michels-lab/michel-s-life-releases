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

## LouderMe — Android direct / sideload

LouderMe source remains private. This repository exposes only what the direct updater needs:

- public release APKs signed with the stable Michel's Lab sideload key;
- SHA-256 checksum files;
- `louderme/latest.json` — machine-readable latest-version manifest.

LouderMe direct builds check that manifest automatically, download the APK, verify its checksum, package identity, version and signing identity, then hand the verified package to Android's installer.

Google Play builds use Google Play's update channel instead.

See `louderme/README.md` for the direct-update contract.

## LouderMe Desktop — Windows

Official public Windows distribution channel for **LouderMe Desktop**.

Normal releases can include:
- `LouderMe-Setup-vX.Y.Z.exe` — recommended Windows installer;
- `LouderMe-vX.Y.Z.exe` — portable self-contained build;
- matching SHA-256 checksum files;
- `louderme-desktop/latest.json` — machine-readable stable-channel manifest.

LouderMe Desktop source remains private. The first Desktop release currently relies on SHA-256 integrity files and does not yet use Windows Authenticode publisher signing.

## Security

Public availability of a binary does not make the proprietary application source open source.

Clients must never require a private GitHub token to check for or download an update.
