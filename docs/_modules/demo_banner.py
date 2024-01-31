def create(demo_name, git_branch):
    introduction = f'You are viewing <strong>{demo_name}</strong>, not the <a href="https://docs.dea.ga.gov.au/">official DEA Knowledge Hub website</a>.'
    build_logs = f'View the <a href="https://app.netlify.com/sites/dea-docs/deploys?filter={git_branch}">build logs for &lsquo;{git_branch}&rsquo; branch</a>.'

    return f'{introduction} {build_logs}'

