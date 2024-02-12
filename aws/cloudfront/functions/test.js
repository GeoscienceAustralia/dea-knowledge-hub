// utils.test.js
const { handler } = require("./redirects.js");
var assert = require("assert");

describe("handler()", () => {
    const tests = [
        { uri: "/index.html", expected: "/" },
        { uri: "/page/index.html", expected: "/page/" },
        { uri: "/example.html", expected: "/example/" },
        { uri: "/foo/example.rst", expected: "/foo/example/" },
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
