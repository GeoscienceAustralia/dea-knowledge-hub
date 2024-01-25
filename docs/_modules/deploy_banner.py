import os

def banner():
    pull_request = os.environ.get("PULL_REQUEST")
    review_id = os.environ.get("REVIEW_ID")
    build_id = os.environ.get("BUILD_ID")
    git_branch = os.environ.get("BRANCH")
    deploy_name = os.environ.get("DEPLOY_NAME")

    knowledge_hub_url = "https://docs.dea.ga.gov.au/"
    github_url = "https://github.com/GeoscienceAustralia/dea-docs"
    deploy_logs_url = "https://app.netlify.com/sites/dea-docs/deploys"

    if pull_request == "true":
        return f'You are viewing <strong>{deploy_name}</strong>, not the <a href="{knowledge_hub_url}">main website</a>. View the <a href="{deploy_logs_url}?filter={git_branch}">deploy logs</a> or <a href="{github_url}/tree/{git_branch}">git branch</a>.'
    else:
        return f'You are viewing <strong>PR #{review_id} {deploy_name}</strong>, not the <a href="{knowledge_hub_url}">main website</a>. View the <a href="{deploy_logs_url}/{build_id}">latest deploy log</a> or the <a href="{github_url}/pull/{review_id}">PR</a>.'

