import os

def banner():
    deploy_name = os.environ.get("DEPLOY_NAME")
    review_id = os.environ.get("REVIEW_ID")
    deploy_id = os.environ.get("DEPLOY_ID")

    knowledge_hub_url = "https://knowledge.dea.ga.gov.au/"
    github_url = "https://github.com/GeoscienceAustralia/dea-knowledge-hub"
    deploy_logs_url = "https://app.netlify.com/sites/dea-docs/deploys"

    return f'You are viewing <strong>{deploy_name} #{review_id}</strong>, not the official <a href="{knowledge_hub_url}">DEA Knowledge Hub</a>. View the <a href="{deploy_logs_url}/{deploy_id}">Deploy log</a> or <a href="{github_url}/pull/{review_id}">Pull request</a>.'

