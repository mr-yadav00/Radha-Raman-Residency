import os
import re

html_files = ['index.html', 'rooms-pricing.html', 'about-contact.html']

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the standalone floating whatsapp button
    content = re.sub(r'<a href=\"https://wa\.me/[^\"]+\" [^>]*floating_whatsapp[^>]*>.*?</a>', '', content, flags=re.DOTALL)

    # HOMEPAGE SEO H1 FIX
    if file == 'index.html':
        content = re.sub(
            r'<h1[^>]*>.*?</h1>',
            '<h1>Radha Raman Residency – Student Hostel in Kota Near Coaching Institutes</h1>',
            content,
            count=1,
            flags=re.DOTALL
        )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# CSS Updates
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

print('Updated successfully.')
