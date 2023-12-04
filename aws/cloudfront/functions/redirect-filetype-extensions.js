// Redirects URLs ending in certain extensions (".html", ".rst", and others) to end in "/" instead. E.g. /page.html => /page/

async function handler(event) {
    const uri = event.request.uri;
    const indexHtmlPattern = /\/index\.html$/g;
    const filetypeExtensionsPattern = /\.(html|rst|md|ipynb|py)$/g;

    if (indexHtmlPattern.test(uri)) {
        return {
            statusCode: 301,
            statusDescription: "Moved Permanently",
            headers: {
                location: {
                    value: uri.replace(indexHtmlPattern, "")
                }
            }
        }
    }

    if (filetypeExtensionsPattern.test(uri)) {
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

    return event.request;
}
