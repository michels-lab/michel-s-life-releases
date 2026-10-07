# LouderMe Desktop — Public Windows Channel

This directory owns the public stable Windows feed for **LouderMe Desktop**.

Windows no longer uses a separate customer-facing release tag. LouderMe publishes one unified release containing the current Android and Windows builds. The unified tag/title identifies both platform versions when they differ.

Windows assets inside that unified release:
- `LouderMe-Setup-vX.Y.Z.exe` — **recommended installer**;
- `LouderMe-Portable-vX.Y.Z.exe` — optional portable self-contained build;
- matching `.sha256` checksum files.

`latest.json` is the machine-readable stable-channel manifest.

The LouderMe source repository remains private. Public binary distribution does not make the application source open source.

Windows Authenticode signing is not yet configured for LouderMe Desktop. SHA-256 files provide integrity verification, but Windows SmartScreen can still warn for an unsigned/new publisher binary.


Both `louderme/latest.json` and `louderme-desktop/latest.json` point to the same unified LouderMe release page while retaining their own platform version metadata.
