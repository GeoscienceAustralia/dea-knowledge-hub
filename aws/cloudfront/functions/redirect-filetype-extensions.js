// Redirects URLs ending in certain extensions (".html", ".rst", and others) to end in "/" instead. E.g. /page.html => /page/

async function handler(event) {
    const uri = event.request.uri;
    const filetypeExtensionsPattern = /\.(html|rst|md|ipynb|py)$/g;

    if (uri.match(filetypeExtensionsPattern)) {
        return {
            statusCode: 301,
            statusDescription: "Moved Permanently",
            headers: {
                location: {
                    value: uri.replace(filetypeExtensionsPattern, "/")
                }
            }
        };
    }

    return request;
}
