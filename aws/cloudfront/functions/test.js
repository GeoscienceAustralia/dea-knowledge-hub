// utils.test.js
const { handler } = require("./redirects.js");
var assert = require("assert");

const docsHost = "docs.dea.ga.gov.au";

function requestTemplate(uri) {
    return {
        request: {
            uri: uri,
            headers: {
                host: {
                    value: docsHost
                }
            }
        }
    };
}

describe("Redirect Tests", () => {
    const redirectTests = [
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

    redirectTests.forEach(({ uri, expected }) => {
        it(`Redirects ${uri} to ${expected}`, async () => {
            const res = await handler(requestTemplate(uri));

            assert.equal(res.headers.location.value, expected);
        });
    });

    const doesntRedirectTests = [
        "/data/product/dea-coastlines/",
        "/data/product/dea-coastlines/?tab=overview",
        "/notebooks/Tools/gen/dea_tools.plotting/",
        "/notebooks/Tools/gen/dea_tools.app.animations/"
    ];

    doesntRedirectTests.forEach(uri => {
        it(`Doesn't redirect ${uri}`, async () => {
            const res = await handler(requestTemplate(uri));

            assert.ok(!res.hasOwnProperty("statusCode"));
            assert.ok(!res.hasOwnProperty("statusDescription"));
        });
    });
});
