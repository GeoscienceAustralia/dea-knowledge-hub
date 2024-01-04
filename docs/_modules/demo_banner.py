def create(demo_name, git_branch, deploy_id):
    alert_text = f'<strong>Note:</strong> You are viewing <strong>{demo_name}</strong> not the <a href="https://docs.dea.ga.gov.au/">official website</a>.'
    menu_text = '<strong>For staff:</strong>'
    git_branch_text = f'On <a href="https://github.com/GeoscienceAustralia/dea-docs/tree/{git_branch}">{git_branch}</a> branch.'
    build_logs_text = f'View the <a href="https://app.netlify.com/sites/dea-docs/deploys?filter={git_branch}">build logs</a>.'

    return " ".join([alert_text, menu_text, git_branch_text, build_logs_text])

