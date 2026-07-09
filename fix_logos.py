import os
import re
import glob

master_logo = """<a href="index.html" class="logo">
    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right: 8px;">
        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke="var(--brand-accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M9 12l2 2 4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    Novus <span>IP</span>
</a>"""

html_files = glob.glob("*.html")

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the header logo
    # Pattern looks for <a href="index.html" class="logo"> ... </a>
    header_pattern = re.compile(r'<a[^>]*class="logo"[^>]*>.*?</a>', re.DOTALL)
    content = header_pattern.sub(master_logo, content)

    # Find the footer logo
    footer_pattern = re.compile(r'<a[^>]*class="logo mb-4 d-inline-block"[^>]*>.*?</a>', re.DOTALL)
    footer_replacement = f'<div class="mb-4 d-inline-block">\n{master_logo}\n</div>'
    content = footer_pattern.sub(footer_replacement, content)

    # Find the auth pages logo
    auth_pattern = re.compile(r'<a[^>]*class="logo mb-4 d-block text-center fs-2"[^>]*>.*?</a>', re.DOTALL)
    auth_replacement = f'<div class="mb-4 d-flex justify-content-center">\n{master_logo}\n</div>'
    content = auth_pattern.sub(auth_replacement, content)

    # Any other logo instances?
    # Let's see if there are other class="logo ..."
    # (Just to be safe, I'll rely on the specific replacements above since those are the known ones)

    # Add favicon if not present
    favicon_html = """<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none'%3E%3Cpath d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z' stroke='%23D4AF37' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3Cpath d='M9 12l2 2 4-4' stroke='%230F172A' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">"""
    
    # Remove existing favicon if it exists to replace it
    content = re.sub(r'<link[^>]*rel=".*?icon"[^>]*>', '', content)
    
    # Insert new favicon before </head>
    content = content.replace('</head>', f'    {favicon_html}\n</head>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done replacing logos and adding favicons.")
