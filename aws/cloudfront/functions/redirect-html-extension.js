// Redirects URLs ending in ".html" to instead end in "/". E.g. /page.html => /page/

async function handler(event) {
    const uri = event.request.uri;
    const htmlExtensionPattern = /.html$/g;

    if (uri.match(htmlExtensionPattern)) {
        return {
            statusCode: 302,
            statusDescription: "Found",
            headers: {
                location: {
                    value: uri.replace(htmlExtensionPattern, "/")
                }
            }
        };
    }

    return request;
}
