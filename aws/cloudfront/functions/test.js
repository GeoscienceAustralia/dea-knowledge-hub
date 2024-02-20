// utils.test.js
const { handler } = require("./redirects.js");
var assert = require("assert");

function 


function requestTemplate(uri) {
    return {
        request: {
            uri: uri,
            headers: {
                host: {
                    value: "docs.dea.ga.gov.au"
                }
            }
        }
    };
}

describe("Test redirect occurs", () => {
    const tests = [
        { uri: "/", expected: "/" },
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
        it(`Correctly redirects ${uri} to ${expected}`, async () => {
            const res = await handler(requestTemplate(uri));

            assert.equal(res.headers.location.value, expected);
        });
    });
});

describe("Test redirect doesn't occur", () => {
    const tests = [
        {
            uri: "/data/product/dea-coastlines/"
        },
        {
            uri: "/data/product/dea-coastlines/?tab=overview"
        },
        {
            uri: "/notebooks/Tools/gen/dea_tools.plotting/"
        },
        {
            uri: "/notebooks/Tools/gen/dea_tools.app.animations/"
        }
    ];

    tests.forEach(({ uri }) => {
        let expected = { uri: uri };
        it(`Doesn't redirect ${uri}`, async () => {
            const res = await handler(requestTemplate(uri));

            assert.deepStrictEqual(res, expected);
        });
    });
});
