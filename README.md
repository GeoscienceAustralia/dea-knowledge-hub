
# Editing and building the DEA docs
>Note: the published version of the docs are **built automatically** by the GitHub pipeline; you don't need to do anything locally after pushing your changes.

## Cloning this repository
```
git clone https://github.com/GeoscienceAustralia/dea-docs.git
cd dea-docs
```

## Building the DEA docs locally for live editing
Local building can be done by running a live server in Docker, which supports live-reloading.
> There is also a legacy approach, retained at the end of this document.

### Build and host in Docker:
```
make fetchnotebooks
make docker-live
```

Notes:
- The `make fetchnotebooks` target downloads the `dea-notebooks` repository to incorporate documentation from there.
If you don't need to see documentation pages from `dea-notebooks` in your live test, it is suggested you *do not* run the  step.

- The `dea-notebooks` repository is very large (~2GB). Therefore:
    - We clone using the flag `--depth 1` (to only fetch the latest commit on the current branch). We specify the branch as `stable` during the clone.
    - The resultant clone is typically a couple of hundred MB.

**Known issues!**
- Local builds with `make fetchnotebooks` currently output a significant number of warnings before stabilising.

## Updating packages
Package versions are pinned in `requirements.txt` and built from `requirements.in` (with less specific pinning). Check the top of `requirements.txt` for info (do not make changes there).
Typically an update will involve:
```
pip install --user pip-tools
pip-compile --output-file=requirements.txt requirements.in
```

## Known issues and areas for future improvement
- DEA docs still uses the `recommonmark` markdown parser, which is no longer supported. It should be switched `sphynx` which DEA internal docs uses. Manual checks for poorly formatted pages will need to be conducted!
- Many pinned package versions are outdated and should be revised.
- There are build issues relating to various pieces of documentation in dea-notebooks. These appear to be breaking relevant parts of the build, causing `dea-notebooks` content not to be output in the live build. This should be investigated, and dependencies updated. It is recommended you do not run `make fetchnotebooks` for now (and in general only if you are specifically interested in how documentation in `dea-notebooks` will be rendered).

## Futher contribution info
See the [contribution instructions](https://github.com/GeoscienceAustralia/dea-docs/wiki/Contribution-instructions) for more details.

## Legacy local build (NOT RECOMMENDED, does not live-reload)
```
conda create -c conda-forge -n deadocs --file requirements.txt
conda activate deadocs
pip install -r requirements.txt
make fetchnotebooks html
open _build/html/index.html
```
> Note: to perform subsequent legacy builds that don't include updates to the `dea-notebooks` repository, you only need to run `make html`.