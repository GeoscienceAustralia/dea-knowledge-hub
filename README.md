# DEA Docs

## Prerequisites

You must have the following installed.

* Git
* Docker

## How to build

**Step 1.** Copy the `.env.example` file and rename it to `.env`. You can configure the following settings.

* `FETCH_NOTEBOOKS` &mdash; `Yes` or `No`
* `BUILD_MODE` &mdash; `Development` or `Production`

**Step 2.** Build and run the Docker image.

```bash
make
```

**Step 3.** Open your web browser at <http://localhost:8011/>

**Step 4.** Edit the content in `/content` then reload the page to see your changes.

## Notes

* Filenames starting with an underscore won't become pages in the output, e.g. `_overview.md`
