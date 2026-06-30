import os

files = [
    'admin-dashboard.html',
    'admin-users.html',
    'admin-devices.html',
    'user-dashboard.html',
    'developer-dashboard.html'
]

for file in files:
    if not os.path.exists(file):
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the main-content mobile css
    old_css = ".main-content { margin-left: 0; padding: 80px 1rem 2rem 1rem; width: 100%; max-width: 100vw; box-sizing: border-box; }"
    new_css = "body { display: block; }\n      .main-content { margin-left: 0; padding: 80px 1rem 2rem 1rem; width: 100%; max-width: 100vw; box-sizing: border-box; min-width: 0; overflow-x: hidden; }"
    
    if old_css in content:
        content = content.replace(old_css, new_css)
    else:
        print(f"Warning: could not find old_css in {file}")
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed mobile overflow in all dashboards.")
