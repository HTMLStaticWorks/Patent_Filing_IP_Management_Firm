import os
import re
import glob

master_logo = """<a href="index.html" class="logo">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-indigo" style="margin-right:8px">
        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
        <path d="M12 8v4"></path>
        <path d="M12 16h.01"></path>
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

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done replacing logos.")
