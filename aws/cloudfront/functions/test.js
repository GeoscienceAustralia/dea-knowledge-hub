
// utils.test.js
const { handler } = require('./redirects.js');
var assert = require('assert');

describe('handler()', () => {

  const tests = [
    {uri: '/index.html', expected: '/'},
    {uri: '/page/index.html', expected: '/page/'},
    {uri: '/example.html', expected: '/example/'},
    {uri: '/foo/example.rst', expected: '/foo/example/'},
    {uri: '/notebooks/Tools/dea_tools/coastal.py', expected: '/notebooks/Tools/gen/dea_tools.coastal/'},
    {uri: '/notebooks/Tools/dea_tools/app/animations.py', expected: '/notebooks/Tools/gen/dea_tools.app.animations/'},
  ];

  tests.forEach(({uri, expected}) => {
    let input = {'request': {'uri': uri}};
    it(`correctly redirects ${uri} to ${expected}`, async () => {
      const res = await handler(input);

      assert.equal(res.headers.location.value, expected);
    });
  });

});
