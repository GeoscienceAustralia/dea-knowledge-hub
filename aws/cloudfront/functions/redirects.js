// This function handles redirect logic

async function handler(event) {
    const request = event.request;
    const uri = event.request.uri;
    const deaToolsSourceCodePattern = /dea_tools\/(.*)\.py$/g;
    const indexHtmlPattern = /\/index\.html$/g;
    const filetypeExtensionsPattern = /\.(html|rst|md|ipynb|py)$/g;

    const status301MovedPermanently = {
        statusCode: 301,
        statusDescription: "Moved Permanently"
    };

    // Redirect DEA Tools source code URLs to the relevant 'automodule' page generated from the source code.
    // E.g. "../Tools/dea_tools/coastal.py" => "/notebooks/Tools/gen/dea_tools.coastal/"

    if (deaToolsSourceCodePattern.test(uri)) {
        const deaToolsName = uri.match(deaToolsSourceCodePattern)[1];
        const deaToolsUri = `/notebooks/Tools/gen/dea_tools.${deaToolsName}/`;
        return {
            ...status301MovedPermanently,
            headers: {
                location: {
                    value: deaToolsUri
                }
            }
        };
    }

    // Redirect URLs ending in "index.html" to end in "/" instead. E.g. /page/index.html => /page/

    if (indexHtmlPattern.test(uri)) {
        return {
            ...status301MovedPermanently,
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
            ...status301MovedPermanently,
            headers: {
                location: {
                    value: uri.replace(filetypeExtensionsPattern, "/")
                }
            }
        };
    }

    return request;
}
