from jinja2 import Environment, FileSystemLoader
import os
import requests
import sys

def main():
    # Configure Jinja2 environment
    env = Environment(loader=FileSystemLoader(os.path.join(
        os.path.dirname(__file__), 
        'templates')
    ))

    # use token
    token = sys.argv[1]

    # Load the template
    template = env.get_template('index.tpl')

    # show languages / tools
    language_icons = [
        'https://img.shields.io/badge/-C-blue?logo=c',
        'https://img.shields.io/badge/-C++-blue?logo=cplusplus',
        'https://img.shields.io/badge/cMake-064F8C?&logo=cmake&logoColor=white',
        'https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54',
        'https://img.shields.io/badge/PHP-777BB4?logo=php&logoColor=white',
        'https://img.shields.io/badge/cakephp-red?logo=cakephp&logoColor=white'
        'https://img.shields.io/badge/asm-6502-orange',
        'https://img.shields.io/badge/asm-z80-orange',
        'https://img.shields.io/badge/asm-8086-orange',
        'https://img.shields.io/badge/Arduino-00878F?logo=arduino&logoColor=fff',
        'https://img.shields.io/badge/-LaTeX-008080&logo=latex&logoColor=white',
        'https://img.shields.io/badge/Sphinx-F7C942&logo=sphinx&logoColor=white',
    ]

    # fetch repo data
    repositories = [
        'hfcxx', 'dftcxx', 'edp', 'den2obj', 'pyqint', 'pydft', 'sphecerix', 'pypwdft'
    ]
    ccp_repositories = []
    for repo in repositories:
        res = fetch_github_repo_details('ifilot', repo, token)
        langs = fetch_github_languages('ifilot', repo, token)
        res['languages'] = dict(list(langs['languages'].items())[:3])
        ccp_repositories.append(res)

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

def fetch_github_repo_details(owner, repo, token):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {
        "Authorization": f"Bearer {token}",
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
            "repo": repo,
        }
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def fetch_github_languages(owner, repo, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/languages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # Calculate the dominant language based on the largest byte count
        dominant_language = max(data, key=data.get) if data else "No languages found"
        return {"languages": data, "dominant_language": dominant_language}
    else:
        print(f"Failed to fetch languages: {response.status_code}")
        return None

if __name__ == '__main__':
    main()