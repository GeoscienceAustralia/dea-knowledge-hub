const { handler } = require("./redirects.js");
var assert = require("assert");

const docsHost = "docs.dea.ga.gov.au";
const knowledgeHost = "knowledge.dea.ga.gov.au";

// This matches the structure of an AWS CloudFront event, albeit with less fields.

function cloudfrontRequestTemplate(host, uri) {
    return {
        request: {
            uri: uri,
            headers: {
                host: {
                    value: host
                }
            }
        }
    };
}

describe("Redirect Tests", () => {
    const tests = [
        { uri: "/index.html", expected: "/" },
        { uri: "/page/index.html", expected: "/page/" },
        { uri: "/category/page.html", expected: "/category/page/" },
        { uri: "/page.html", expected: "/page/" },
        { uri: "/page.rst", expected: "/page/" },
        { uri: "/page.md", expected: "/page/" },
        { uri: "/page.ipynb", expected: "/page/" },
        { uri: "/page.py", expected: "/page/" },
        {
            uri: "/notebooks/Beginners_guide/Tools/dea_tools/plotting.py",
            expected: "/notebooks/Tools/gen/dea_tools.plotting/"
        },
        {
            uri: "/notebooks/Interactive_apps/Tools/dea_tools/app/animations.py",
            expected: "/notebooks/Tools/gen/dea_tools.app.animations/"
        }
    ];

    tests.forEach(({ uri, expected }) => {
        it(`Redirects ${uri} to ${expected}`, async () => {
            const res = await handler(
                cloudfrontRequestTemplate(knowledgeHost, uri)
            );

            assert.equal(res.headers.location.value, expected);
        });
    });
});

describe("Doesn't Redirect Tests", () => {
    const tests = [
        "/data/product/dea-coastlines/",
        "/data/product/dea-coastlines/?tab=overview",
        "/notebooks/Tools/gen/dea_tools.plotting/",
        "/notebooks/Tools/gen/dea_tools.app.animations/"
    ];

    tests.forEach(uri => {
        it(`Doesn't redirect ${uri}`, async () => {
            const res = await handler(
                cloudfrontRequestTemplate(knowledgeHost, uri)
            );

            assert.ok(!res.hasOwnProperty("statusCode"));
            assert.ok(!res.hasOwnProperty("statusDescription"));
        });
    });
});

describe("Domain Redirect Tests", () => {
    const tests = [
        "/",
        "/index.html",
        "/data/product/dea-coastlines/",
        "/data/product/dea-coastlines/?tab=overview"
    ];

    tests.forEach(uri => {
        const docsUri = "https://" + docsHost + uri;
        const knowledgeUri = "https://" + knowledgeHost + uri;

        it(`Redirects from ${docsUri} to ${knowledgeUri}`, async () => {
            const res = await handler(cloudfrontRequestTemplate(docsHost, uri));

            assert.equal(res.headers.location.value, knowledgeUri);
        });
    });
});
