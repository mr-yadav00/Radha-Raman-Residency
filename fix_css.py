import os
import re

css_file = 'assets/css/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace body padding-bottom on mobile to 80px
css = re.sub(r'body\{padding-bottom:60px\}', 'body{padding-bottom:80px}', css)

# Hide .float-widgets on mobile
css = re.sub(
    r'@media \(max-width:768px\)\{',
    '@media (max-width:768px){.float-widgets{display:none !important;}',
    css
)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated css successfully.')

