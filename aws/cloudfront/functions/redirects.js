// AWS CloudFront redirects
// Learn how to test and deploy these redirects:
// https://docs.dev.dea.ga.gov.au/public_services/dea_knowledge_hub/aws_redirects.html

// This function handles redirect logic

async function handler(event) {
    const request = event.request;
    const host = event.request.headers.host.value;
    const uri = event.request.uri;

    const deaToolsSourceCodePattern = /dea_tools\/(.*)\.py$/;
    const indexHtmlPattern = /\/index\.html$/g;
    const filetypeExtensionsPattern = /\.(html|rst|md|ipynb|py)$/g;

    const docsHost = "docs.dea.ga.gov.au";
    const knowledgeHost = "knowledge.dea.ga.gov.au";

    const status301MovedPermanently = {
        statusCode: 301,
        statusDescription: "Moved Permanently"
    };

    // Redirect subdomain from 'docs' to 'knowledge'. E.g. "docs.dea.ga.gov.au" => "knowledge.dea.ga.gov.au"

    if (host === docsHost) {
        return Object.assign(status301MovedPermanently, {
            headers: {
                location: {
                    value: "https://" + knowledgeHost + uri
                }
            }
        });
    }

    // Redirect DEA Tools source code URLs to the relevant 'automodule' page generated from the source code.
    // E.g. "/notebooks/Beginners_guide/Tools/dea_tools/plotting.py" => "/notebooks/Tools/gen/dea_tools.plotting/"
    // E.g. "/notebooks/Interactive_apps/Tools/dea_tools/app/animations.py" => "/notebooks/Tools/gen/dea_tools.app.animations/"

    if (deaToolsSourceCodePattern.test(uri)) {
        const automoduleName = deaToolsSourceCodePattern
            .exec(uri)[1]
            .replaceAll("/", ".");
        const automoduleUri = `/notebooks/Tools/gen/dea_tools.${automoduleName}/`;

        return Object.assign(status301MovedPermanently, {
            headers: {
                location: {
                    value: automoduleUri
                }
            }
        });
    }

    // Redirect URLs ending in "index.html" to end in "/" instead. E.g. /page/index.html => /page/

    if (indexHtmlPattern.test(uri)) {
        return Object.assign(status301MovedPermanently, {
            headers: {
                location: {
                    value: uri.replace(indexHtmlPattern, "/")
                }
            }
        });
    }

    // Redirect URLs ending in certain extensions (".html", ".rst", and others) to end in "/" instead. E.g. /example.html => /example/

    if (filetypeExtensionsPattern.test(uri)) {
        return Object.assign(status301MovedPermanently, {
            headers: {
                location: {
                    value: uri.replace(filetypeExtensionsPattern, "/")
                }
            }
        });
    }

    return request;
}

module.exports = { handler };
