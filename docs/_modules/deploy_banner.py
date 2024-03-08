import os

def banner():
    git_branch = os.environ.get("BRANCH")
    deploy_name = os.environ.get("DEPLOY_NAME")
    pull_request = os.environ.get("PULL_REQUEST")
    review_id = os.environ.get("REVIEW_ID")
    deploy_id = os.environ.get("DEPLOY_ID")

    knowledge_hub_url = "https://knowledge.dea.ga.gov.au/"
    github_url = "https://github.com/GeoscienceAustralia/dea-knowledge-hub"
    deploy_logs_url = "https://app.netlify.com/sites/dea-docs/deploys"

    pull_request_banner = f'You are viewing <strong>{deploy_name} #{review_id}</strong>, not the official <a href="{knowledge_hub_url}">DEA Knowledge Hub</a>. View the <a href="{deploy_logs_url}/{deploy_id}">Deploy log</a> or <a href="{github_url}/pull/{review_id}">Pull request</a>.'

    demo_banner = f'You are viewing <strong>{deploy_name}</strong>, not the official <a href="{knowledge_hub_url}">DEA Knowledge Hub</a>. View the <a href="{deploy_logs_url}?filter={git_branch}">Deploy logs</a> or <a href="{github_url}/tree/{git_branch}">Git branch</a>.'

    if pull_request == "true":
        return pull_request_banner
    else:
        return demo_banner

