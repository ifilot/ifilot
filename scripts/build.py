from jinja2 import Environment, FileSystemLoader
import os

# Configure Jinja2 environment
env = Environment(loader=FileSystemLoader(os.path.join([os.path.dirname(__file__), 'templates'])))

# Load the template
template = env.get_template('index.tpl')

# Define the data to pass to the template
data = {
    "title": "My Jinja2 Page",
    "message": "This is a minimal example of rendering a webpage with Jinja2.",
    "items": ["Item 1", "Item 2", "Item 3"]
}

# Render the template with the data
output = template.render(data)

# Write the rendered HTML to a file
with open("README.md", "w") as f:
    f.write(output)
