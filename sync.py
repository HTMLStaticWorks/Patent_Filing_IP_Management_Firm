import os
import re

TARGET_FILES = [
    'index-2.html', 'about.html', 'services.html', 'service-details.html',
    'blog.html', 'blog-details.html', 'pricing.html', 'gallery.html',
    'booking.html', 'contact.html', '404.html', 'coming-soon.html'
]

def extract_section(content, start_marker, end_marker):
    pattern = re.compile(rf'({start_marker}.*?{end_marker})', re.DOTALL)
    match = pattern.search(content)
    return match.group(1) if match else None

def replace_section(content, start_marker, end_marker, new_section):
    pattern = re.compile(rf'{start_marker}.*?{end_marker}', re.DOTALL)
    return pattern.sub(new_section.replace('\\', '\\\\'), content)

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

header_html = extract_section(index_content, r'<!-- Header -->\s*<header class="site-header">', r'</header>')
footer_html = extract_section(index_content, r'<!-- Footer -->\s*<footer class="site-footer">', r'</footer>')

for filename in TARGET_FILES:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace Header
        if header_html:
            content = replace_section(content, r'<!-- Header -->\s*<header class="site-header">', r'</header>', header_html)
            
        # Replace Footer
        if footer_html:
            content = replace_section(content, r'<!-- Footer -->\s*<footer class="site-footer">', r'</footer>', footer_html)
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Synced {filename}")
    else:
        print(f"File {filename} not found.")
