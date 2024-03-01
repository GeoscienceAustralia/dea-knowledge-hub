// utils.test.js
const { handler } = require("./redirects.js");
var assert = require("assert");

const docsHost = "docs.dea.ga.gov.au";
const knowledgeHost = "knowledge.dea.ga.gov.au";

// Create a minimum event object matching the structure that AWS CloudFront uses.
// The real thing contains many more fields, this is just what we use.
function requestTemplate(host, uri) {
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
    const r1 = [
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

    r1.forEach(({ uri, expected }, index) => {
        const n = index + 1;
        it(`R1.${n}. Redirects ${uri} to ${expected}`, async () => {
            const res = await handler(requestTemplate(knowledgeHost, uri));

            assert.equal(res.headers.location.value, expected);
        });
    });
});

describe("Don't Redirect Tests", () => {
    const r2 = [
        "/data/product/dea-coastlines/",
        "/data/product/dea-coastlines/?tab=overview",
        "/notebooks/Tools/gen/dea_tools.plotting/",
        "/notebooks/Tools/gen/dea_tools.app.animations/"
    ];

    r2.forEach((uri, index) => {
        const n = index + 1;
        it(`R2.${n}. Doesn't redirect ${uri}`, async () => {
            const res = await handler(requestTemplate(knowledgeHost, uri));

            assert.ok(!res.hasOwnProperty("statusCode"));
            assert.ok(!res.hasOwnProperty("statusDescription"));
        });
    });
});

describe("Domain redirection tests", () => {
    const r3 = [
        "/",
        "/index.html",
        "/data/product/dea-coastlines/",
        "/data/product/dea-coastlines/?tab=overview"
    ];

    r3.forEach((uri, index) => {
        const docsUri = "https://" + docsHost + uri;
        const knowledgeUri = "https://" + knowledgeHost + uri;

        const n = index + 1;
        it(`R3.${n}. Redirects from ${docsUri} to ${knowledgeUri}`, async () => {
            const res = await handler(requestTemplate(docsHost, uri));

            assert.equal(res.headers.location.value, knowledgeUri);
        });
    });
});
