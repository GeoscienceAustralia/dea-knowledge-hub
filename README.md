# DEA Docs

## Prerequisites

You must have the following installed on your computer.

* Git
* Docker

## How to build

**Step 1.** Clone this git repository to your local computer then enter the folder.

```bash
git clone --depth 1 --branch dea-docs-v2 git@github.com:GeoscienceAustralia/dea-docs.git
```

**Step 2.** Copy the `.env.example` file to a new file named `.env`. In this file, you can configure the following settings.

* `FETCH_NOTEBOOKS` &mdash; `Yes` or `No`
* `BUILD_MODE` &mdash; `Development` or `Production`

**Step 3.** Build and run the Docker image by running the following command.

```bash
make
```

**Step 4.** Open your web browser at <http://localhost:8011/>

**Step 5.** Edit the content in `/content` then reload the page to see your changes.

## Notes

* Filenames starting with an underscore won't become pages in the output, e.g. `_overview.md`
