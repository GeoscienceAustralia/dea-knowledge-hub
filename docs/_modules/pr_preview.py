import os

def banner():
    pull_request_number = os.environ.get("PULL_REQUEST_NUMBER")
    deploy_log_url = os.environ.get("PR_PREVIEW_DEPLOY_LOG_URL")

    knowledge_hub_url = "https://knowledge.dea.ga.gov.au/"
    github_url = "https://github.com/GeoscienceAustralia/dea-knowledge-hub"

    return f'You are viewing <strong>Pull Request #{pull_request_number}</strong>, not the official <a href="{knowledge_hub_url}">DEA Knowledge Hub</a>. View the <a href="{github_url}/pull/{pull_request_number}">Pull request</a> or <a href="{deploy_log_url}">Deploy log</a>.'

