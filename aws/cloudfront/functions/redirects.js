const responseCode301 = {
    statusCode: 301,
    statusDescription: "Moved Permanently"
};

async function handler(event) {
    const request = event.request;
    const uri = event.request.uri;
    const indexHtmlPattern = /\/index\.html$/g;
    const pythonExtensionPattern = /\.py$/g;
    const filetypeExtensionsPattern = /\.(html|rst|md|ipynb|py)$/g;

    // Redirect URLs ending in ".py"

    if (pythonExtensionPattern.text(uri)) {
        return {
            ...responseCode301,
            headers: {
                location: {
                    value: uri.replace(indexHtmlPattern, "/")
                }
            }
        };
    }

    // Redirect URLs ending in "index.html" to end in "/" instead. E.g. /page/index.html => /page/

    if (indexHtmlPattern.test(uri)) {
        return {
            ...responseCode301,
            headers: {
                location: {
                    value: uri.replace(indexHtmlPattern, "/")
                }
            }
        };
    }

    // Redirect URLs ending in certain extensions (".html", ".rst", and others) to end in "/" instead. E.g. /example.html => /example/

    if (filetypeExtensionsPattern.test(uri)) {
        return {
            ...responseCode301,
            headers: {
                location: {
                    value: uri.replace(filetypeExtensionsPattern, "/")
                }
            }
        };
    }

    return request;
}
