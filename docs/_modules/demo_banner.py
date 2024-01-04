def create(demo_name, git_branch, deploy_id):
    return f"You are viewing <strong>{demo_name}</strong> on <a href=\"https://github.com/GeoscienceAustralia/dea-docs/tree/{git_branch}\">{git_branch}</a> branch. <a href=\"https://app.netlify.com/sites/dea-docs/deploys/{deploy_id}\">View the build log</a>. <a href=\"https://docs.dea.ga.gov.au/\" target=\"_self\">Go to the main website</a>."
