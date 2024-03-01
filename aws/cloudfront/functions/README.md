# AWS CloudFront Redirects

## Deployment

Currently deployed by hand through the AWS Console.

1. Log in to the AWS Console.
2. Navigate to https://us-east-1.console.aws.amazon.com/cloudfront/v3/home#/functions in the `ga-aws-dea-data` Account.
3. Select the `RewriteIndexHTMLURLs` function.
4. Replace the function code with the contents for `redirects.js`, **Remove** the last line  `module.exports = { handler };`. It's currently required for the tests, but is incompatible with CloudFront Functions.
5. Save Changes.
6. Run a few tests using the `Test` tab.
7. When you're happy, `Publish`.

## Tests

Run: `npx mocha`
