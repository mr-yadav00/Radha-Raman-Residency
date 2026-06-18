import re

with open('404.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <title>
content = re.sub(r'<title>.*?</title>', '<title>Page Not Found - Radha Raman Residency</title>', content)

# Remove all <main> content
new_main = """
<main id="main-content" style="min-height: 70vh; display: flex; align-items: center; justify-content: center; text-align: center; padding: 100px 20px;">
    <div>
        <h1 style="font-family: 'Playfair Display', serif; font-size: clamp(4rem, 8vw, 6rem); color: var(--gold); margin-bottom: 20px;">404</h1>
        <h2 style="font-family: 'Playfair Display', serif; font-size: 2rem; color: var(--deep); margin-bottom: 20px;">Page Not Found</h2>
        <p style="color: var(--muted); margin-bottom: 40px; font-size: 1.1rem; max-width: 500px; margin-left: auto; margin-right: auto;">The page you are looking for doesn't exist or has been moved.</p>
        <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
            <a href="/Radha-Raman-Residency/" class="btn-primary">Return Home</a>
            <a href="/Radha-Raman-Residency/about-contact#contact" class="btn-outline">Contact Us</a>
        </div>
    </div>
</main>
"""

content = re.sub(r'<main id="main-content">.*?</main>', new_main, content, flags=re.DOTALL)

with open('404.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("404.html created.")
