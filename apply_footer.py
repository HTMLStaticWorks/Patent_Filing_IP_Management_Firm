import os
import re

source_file = 'index-2.html'
target_files = [
    'index.html', 'about.html', 'services.html', 'service-details.html',
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

# 1. Extract footer from index-2.html
with open(source_file, 'r', encoding='utf-8') as f:
    source_content = f.read()

footer_html = extract_section(source_content, r'<!-- Footer -->\s*<footer class="site-footer">', r'</footer>')

if not footer_html:
    print("Could not find footer in index-2.html!")
    exit(1)

# 2. Apply to all target files
for filename in target_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = replace_section(content, r'<!-- Footer -->\s*<footer class="site-footer">', r'</footer>', footer_html)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated footer in {filename}")
    else:
        print(f"File {filename} not found.")
