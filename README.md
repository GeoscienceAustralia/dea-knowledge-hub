# DEA Docs

**Step 1.** Copy the `.env.example` file and rename it to `.env`. You can configure the following settings.

* `FETCH_NOTEBOOKS` &mdash; `Yes` or `No`
* `BUILD_MODE` &mdash; `Development` or `Production`

**Step 2.** Build and run the Docker image.

```bash
make
```

**Step 3.** Open your web browser at <http://localhost:8011/>

**Step 4.** Edit the content in `/content` then reload the page to see your changes.
