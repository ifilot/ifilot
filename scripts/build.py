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

    # Load the template
    template = env.get_template('index.tpl')

    # show languages / tools
    language_icons = [
        'https://img.shields.io/badge/-C-blue?logo=c&logoColor=white',
        'https://img.shields.io/badge/-C++-blue?logo=cplusplus',
        'https://img.shields.io/badge/cMake-064F8C?&logo=cmake&logoColor=white',
        'https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54',
        'https://img.shields.io/badge/PHP-777BB4?logo=php&logoColor=white',
        'https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=fff',
        'https://img.shields.io/badge/cakephp-red?logo=cakephp&logoColor=white'
        'https://img.shields.io/badge/asm-6502-orange',
        'https://img.shields.io/badge/asm-z80-orange',
        'https://img.shields.io/badge/asm-8086-orange',
        'https://img.shields.io/badge/Arduino-00878F?logo=arduino&logoColor=fff',
        'https://img.shields.io/badge/-LaTeX-008080?logo=latex&logoColor=white',
        'https://img.shields.io/badge/Sphinx-F7C942?logo=sphinx&logoColor=white',
        'https://img.shields.io/badge/Blender-%23F5792A.svg?logo=blender&logoColor=white',
        'https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff',
        'https://img.shields.io/badge/Django-%23092E20.svg?logo=django&logoColor=white',
        'https://img.shields.io/badge/Debian-A81D33?logo=debian&logoColor=fff',
        'https://img.shields.io/badge/Ubuntu-E95420?logo=ubuntu&logoColor=white',
        'https://img.shields.io/badge/Ubuntu-E95420?logo=ubuntu&logoColor=white',
        'https://img.shields.io/badge/Sublime%20Text-%23575757.svg?logo=sublime-text&logoColor=important',
        'https://img.shields.io/badge/Vim-%2311AB00.svg?logo=vim&logoColor=white',
        'https://img.shields.io/badge/Notepad++-90E59A.svg?&logo=notepad%2b%2b&logoColor=black',
        'https://img.shields.io/badge/-RaspberryPi-C51A4A?logo=Raspberry-Pi',
    ]

    ccp_repositories = get_repo_data([
        'pyqint', 
        'pydft', 
        'pypwdft',
        'hfcxx', 
        'dftcxx', 
        'edp', 
        'den2obj', 
        'sphecerix', 
        'bramble'
    ])

    p2k_repositories = get_repo_data([
        'p2000t-sdcard', 
        'p2000t-cartridges',
        'p2000t-cartridge-reader',
        'p2000c-bytebridge-8086',
    ])

    oshw_repositories = get_repo_data([
        'pico-sst39sf0x0-programmer',
        'pico-flasher-cli',
    ])

    # Define the data to pass to the template
    data = {
        'language_icons' : language_icons,
        'ccp_repositories' : ccp_repositories,
        'p2k_repositories' : p2k_repositories,
        'oshw_repositories' : oshw_repositories,
    }

    # Render the template with the data
    output = template.render(data)

    # Write the rendered HTML to a file
    with open("README.md", "w") as f:
        f.write(output)

def get_repo_data(repositories):
    """
    Grab repository information by supplying repository names
    """
    # use token
    token = sys.argv[1]

    repos = []
    for repo in repositories:
        res = fetch_github_repo_details('ifilot', repo, token)
        res['languages'] = fetch_github_languages('ifilot', repo, token)[:2]
        repos.append(res)
    return repos

def fetch_github_repo_details(owner, repo, token):
    """
    Fetch repository information like number of stars, open issues, forks,
    description and html link.
    """
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

def fetch_github_languages(owner, repo, token=None):
    """
    Fetch dominant language of repository
    """
    # Fetch languages from the GitHub API
    api_url = f"https://api.github.com/repos/{owner}/{repo}/languages"
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    response = requests.get(api_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch languages: {response.status_code}")
        return None
    
    languages = response.json()
    
    # Fetch language colors
    colors_response = requests.get("https://raw.githubusercontent.com/ozh/github-colors/master/colors.json")
    if colors_response.status_code != 200:
        print("Failed to fetch language colors.")
        return None
    
    colors = colors_response.json()
    
    # Match languages with their colors
    language_data = []
    for lang, bytes_count in languages.items():
        color = colors.get(lang, {}).get("color", "#CCCCCC")  # Default to grey if no color found
        language_data.append({
            "language": lang,
            "bytes": bytes_count,
            "color": color,
        })
    
    return language_data

if __name__ == '__main__':
    main()