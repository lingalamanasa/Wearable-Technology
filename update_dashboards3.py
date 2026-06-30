import os
import re

files = [
    'admin-dashboard.html',
    'admin-users.html',
    'admin-devices.html',
    'user-dashboard.html',
    'developer-dashboard.html'
]

home_link = '      <a href="index.html"><i class="bi bi-house-door"></i> Back to Home</a>\n    </nav>'

for file in files:
    if not os.path.exists(file):
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. Fix mobile viewport height issue for the sidebar so the footer isn't cut off
    content = content.replace(
        '.sidebar {\n      width: 270px; min-height: 100vh;',
        '.sidebar {\n      width: 270px; height: 100dvh;'
    )
    # Handle inline cases if any
    content = content.replace(
        'width: 270px; min-height: 100vh; background',
        'width: 270px; height: 100%; min-height: 100dvh; background'
    )
    
    # 2. Add Back to Home link to the end of the sidebar-nav
    if '<a href="index.html"><i class="bi bi-house-door"></i> Back to Home</a>' not in content:
        content = content.replace('    </nav>', home_link)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated dashboards with Back to Home link and fixed sidebar height.")
