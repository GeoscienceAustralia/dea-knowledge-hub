// Redirects URLs ending in certain extensions (".html", ".rst", and others) to end in "/" instead. E.g. /page.html => /page/

async function handler(event) {
    const uri = event.request.uri;
    const filetypeExtensionPattern = /.(html|rst|md|ipynb)$/g;

    if (uri.match(filetypeExtensionPattern)) {
        return {
            statusCode: 301,
            statusDescription: "Moved Permanently",
            headers: {
                location: {
                    value: uri.replace(filetypeExtensionPattern, "/")
                }
            }
        };
    }

    return request;
}
