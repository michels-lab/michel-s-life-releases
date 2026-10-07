# LouderMe Desktop — Public Windows Channel

This directory owns the public stable Windows feed for **LouderMe Desktop**.

Published releases use tags:

`louderme-desktop-vX.Y.Z`

Normal release assets:
- `LouderMe-Setup-vX.Y.Z.exe` — **recommended installer**;
- `LouderMe-Portable-vX.Y.Z.exe` — optional portable self-contained build;
- matching `.sha256` checksum files.

`latest.json` is the machine-readable stable-channel manifest.

The LouderMe source repository remains private. Public binary distribution does not make the application source open source.

Windows Authenticode signing is not yet configured for LouderMe Desktop. SHA-256 files provide integrity verification, but Windows SmartScreen can still warn for an unsigned/new publisher binary.
