# DEA Docs

## Prerequisites

You must have the following installed on your computer.

* Git
* Docker

All the other dependencies are installed automatically by Docker. It installs them inside a 'container', so it doesn't install anything on your operating system and it doesn't affect your existing Python version.

## How to build

Types of builds:

* **Local** -- uses Docker.
* **Demo** -- uses Netlify.
* **Production** -- uses S3, Cloudfront, and GitHub Actions.

### Local build

**Step 1.** Clone this git repository to your local computer then enter the folder.

```bash
git clone --depth 1 --branch dea-docs-v2 git@github.com:GeoscienceAustralia/dea-docs.git
```

**Step 2.** Copy the `.env.example` file to a new file named `.env`.

**Step 3.** Build and run the Docker image.

If you are using Mac or Linux, run:

```Shell
make
```

Or, if you are using Windows, run:

```Batchfile
make.cmd
```

**Step 4.** Open your web browser at <http://localhost:8011/>

**Step 5.** Edit the content in `/content` then reload the page to see your changes.

### Demo build

You will need to overwrite one of the demo branches (`demo1`, `demo2`, or `demo3`) with your feature branch.

```
git checkout feature-branch
git merge -s ours demo1
git checkout demo1
git merge feature-branch
```

## Notes

* Filenames starting with an underscore won't become pages in the output, e.g. `_overview.md`
