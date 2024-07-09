# How to make a release

`jupyter-launcher-shortcuts` is a package available on [PyPI]. These are
instructions on how to make a release.

## Pre-requisites

- Push rights to [github.com/2i2c-org/jupyter-launcher-shortcuts]

## Steps to make a release

1. Create a PR updating `yarn.lock` and continue only when its merged.

   This helps us avoid leaving known vulnerabilities are unfixed. To do this,
   delete the file and manually perform the the `build dist` step in the
   `.github/workflows/release.yaml` workflow's `build` job as summarized below.

   ```shell
   # git clean -xfd can be needed to ensure yarn.lock
   # gets re-created during pyproject-build
   rm yarn.lock

   pip install --upgrade pip build
   pyproject-build
   ```

2. Create a PR updating `CHANGELOG.md` with [github-activity] and continue only
   when its merged.

3. Checkout main and make sure it is up to date.

   ```shell
   git checkout main
   git fetch origin main
   git reset --hard origin/main
   ```

4. Update the version, make commits, and push a git tag with `tbump`.

   ```shell
   pip install tbump
   tbump --dry-run ${VERSION}

   # run
   tbump ${VERSION}
   ```

   Following this, the [CI system] will build and publish a release.

5. Reset the version back to dev, e.g. `4.0.1-0.dev` after releasing `4.0.0`.

   ```shell
   tbump --no-tag ${NEXT_VERSION}-0.dev
   ```

[github-activity]: https://github.com/executablebooks/github-activity
[github.com/2i2c-org/jupyter-launcher-shortcuts]: https://github.com/2i2c-org/jupyter-launcher-shortcuts
[pypi]: https://pypi.org/project/jupyter-launcher-shortcuts/
[ci system]: https://github.com/2i2c-org/jupyter-launcher-shortcuts/actions/workflows/release.yaml
