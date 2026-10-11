# Split LouderMe releases out of Michel's Life (2026-10-11)

## Confirmed defect

`michels-lab/michel-s-life-releases` currently hosts the Michel's Life customer releases **and** LouderMe customer releases. Three LouderMe publisher workflows and two LouderMe feeds in this repository explicitly point into the wrong product's release history. Installed LouderMe Android and Windows clients also hard-code the legacy feed URLs.

## Target

- Michel's Life: `michels-lab/michel-s-life-releases` — only Michel's Life builds and update endpoints.
- LouderMe: `michels-lab/LouderMe-releases` — only LouderMe releases; **the same LouderMe tag includes the corresponding Android APK and Windows Setup/Portable binaries**.
- Michel's Lab standards remain in `michels-lab/Michel-Software-Standards`.
- Do not republish or modify Michel's Life binaries merely to separate publication channels.

## Mandatory order of operations

1. Create a **public**, initialized `michels-lab/LouderMe-releases` repository under the Michel's Lab organization with a `main` branch. The present GitHub connector cannot create a repository. No personal access token or signing material is needed.
2. Place `migration/import-louderme-history.workflow.yml` from this migration branch into **the new repository** as `.github/workflows/import-louderme-history.yml`. It intentionally does not execute inside this legacy release repository.
3. Trigger the new repository's import workflow (dispatch, or push `migration/START.json` into its main branch). It copies the historical `louderme-*` releases in timestamp order, verifies existing source checksums and checks target release asset names and byte sizes, and publishes new `louderme/latest.json` and `louderme-desktop/latest.json` under the new repository. The workflow fails closed if links are unavailable. Old binaries are not removed.
4. Independently verify current Android APK and Windows Setup/Portable downloads from **the new URL**, hashes, installer/app identities, stable tags, and the source provenance. Re-run this verification on the actual destination before cutover.
5. Redirect the **old** `louderme/latest.json` and `louderme-desktop/latest.json` URLs to the verified **new** LouderMe release assets. This step keeps existing Android/Windows installations that permanently query the old manifest URLs functioning.
6. Change `LouderMe` Android `DirectUpdateConfig.kt`, Windows `DesktopUpdateService.cs`, its docs and all LouderMe publisher target/feed URLs to use `michels-lab/LouderMe-releases`. The new source builds must use the new feed. Ensure the new repository has its own future publish workflows (new dedicated repo GITHUB_TOKEN or a narrowly scoped, authorized publisher), then disable/remove the three LouderMe publish workflows from the Michel's Life release repo.
7. Validate a new LouderMe release: separate same-release Android/Windows artifacts, both feeds, checksums, in-place updates from existing Android/Windows binaries, and **no new LouderMe release in Michel's Life repo**.
8. Retire legacy LouderMe release entries only once all legacy direct download URLs have been assessed for backward compatibility. Deleting releases immediately makes previously distributed pinned download links return 404 even when the updater feed has been redirected. Keep exact historic downloads intact until a deliberate retention decision.

## Readiness / safety state

- **Prepared**: destination-side import workflow in a non-production migration branch. No change to shipping app binaries, production manifests, existing releases or release publishers.
- **Blocked**: `michels-lab/LouderMe-releases` does not exist as of the 2026-10-11 check; the GitHub connector exposes repository edits but not repository creation.
- **Never** delete old releases or disable legacy updates before new destination checks pass.
- **Never** infer a successful migration from committed YAML alone. CI execution, destination release verification, and real updater testing are required.

## Useful anchors

- Old releases: https://github.com/michels-lab/michel-s-life-releases/releases
- LouderMe source: https://github.com/michels-lab/LouderMe
- Desired dedicated LouderMe channel: https://github.com/michels-lab/LouderMe-releases
