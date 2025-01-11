from jinja2 import Environment, FileSystemLoader
import os

# Configure Jinja2 environment
env = Environment(loader=FileSystemLoader(os.path.join(
    os.path.dirname(__file__), 
    'templates')
))

# Load the template
template = env.get_template('index.tpl')

language_icons = [
    'https://img.shields.io/badge/-C-blue?logo=c',
    'https://img.shields.io/badge/-C++-blue?logo=cplusplus',
    'https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54',
    'https://img.shields.io/badge/PHP-777BB4?logo=php&logoColor=white',
    'https://img.shields.io/badge/cakephp-red?logo=cakephp&logoColor=black'
]

# Define the data to pass to the template
data = {
    'language_icons' : language_icons
}

# Render the template with the data
output = template.render(data)

# Write the rendered HTML to a file
with open("README.md", "w") as f:
    f.write(output)
