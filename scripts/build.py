from jinja2 import Environment, FileSystemLoader
import os
import requests

def main():
    # Configure Jinja2 environment
    env = Environment(loader=FileSystemLoader(os.path.join(
        os.path.dirname(__file__), 
        'templates')
    ))

    # Load the template
    template = env.get_template('index.tpl')

    # show languages / tools
    language_icons = [
        'https://img.shields.io/badge/-C-blue?logo=c',
        'https://img.shields.io/badge/-C++-blue?logo=cplusplus',
        'https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54',
        'https://img.shields.io/badge/PHP-777BB4?logo=php&logoColor=white',
        'https://img.shields.io/badge/cakephp-red?logo=cakephp&logoColor=white'
        'https://img.shields.io/badge/asm-6502-orange',
        'https://img.shields.io/badge/asm-z80-orange',
        'https://img.shields.io/badge/asm-8086-orange',
    ]

    # fetch repo data
    repositories = [
        'hfcxx', 'dftcxx', 'edp', 'den2obj', 'pyqint', 'pydft', 'sphecerix', 'pypwdft'
    ]
    ccp_repositories = []
    for repo in repositories:
        ccp_repositories.append(fetch_github_repo_details('ifilot', repo))

    # Define the data to pass to the template
    data = {
        'language_icons' : language_icons,
        'ccp_repositories' : ccp_repositories
    }

    # Render the template with the data
    output = template.render(data)

    # Write the rendered HTML to a file
    with open("README.md", "w") as f:
        f.write(output)

def fetch_github_repo_details(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        stars = data.get("stargazers_count", 0)
        issues = data.get("open_issues_count", 0)
        link = data.get("html_url", "No link available")
        forks = data.get("forks_count", 0)
        description = data.get("description", "No description available")
        return {
            "stars": stars,
            "issues": issues,
            "forks": forks,
            "description": description,
            "link": link,
        }
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    
if __name__ == '__main__':
    main()