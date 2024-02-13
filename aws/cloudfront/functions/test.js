// utils.test.js
const { handler } = require("./redirects.js");
var assert = require("assert");

describe("Test redirect occurs", () => {
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
        let input = { request: { uri: uri } };
        it(`Correctly redirects ${uri} to ${expected}`, async () => {
            const res = await handler(input);

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
        let input = { request: { uri: uri } };
        let expected = { uri: uri };
        it(`Doesn't redirect ${uri}`, async () => {
            const res = await handler(input);

            assert.deepStrictEqual(res, expected);
        });
    });
});
