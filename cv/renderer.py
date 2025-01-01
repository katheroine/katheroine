import os
import yaml
from jinja2 import Environment, FileSystemLoader

# Set up the Jinja2 environment
current_directory = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_directory))

# Load the template
template = env.get_template('template.html')

# Load context data from YAML file
with open('context.yml', 'r') as file:
    context = yaml.safe_load(file)

# Render the template with context data
rendered_html = template.render(context)

# Optionally, save to an HTML file
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(rendered_html)
