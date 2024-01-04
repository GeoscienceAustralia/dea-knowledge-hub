const responseCode301 = {
    statusCode: 301,
    statusDescription: "Moved Permanently"
};

async function handler(event) {
    const request = event.request;
    const uri = event.request.uri;
    const deaToolsSourceCodePattern = /dea_tools\/(.*)\.py$/g;
    const indexHtmlPattern = /\/index\.html$/g;
    const filetypeExtensionsPattern = /\.(html|rst|md|ipynb|py)$/g;

    // Redirect 'DEA Tools' source code URLs to the 'automodule' page generated from the source code.

    if (deaToolsSourceCodePattern.test(uri)) {
        const toolName = uri.match(deaToolsSourceCodePattern);
        const toolUri = `/notebooks/Tools/gen/dea_tools.${toolName}/`;
        return {
            ...responseCode301,
            headers: {
                location: {
                    value: toolUri
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
