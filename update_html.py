import os
import re

base_dir = r"c:\Users\manu1\OneDrive\Desktop\Wearable Technology"
files_to_update = ["index.html", "about.html", "services.html", "blog.html", "contact.html"]

login_tag = '<a href="login.html" class="btn-primary"><i class="bi bi-person-circle"></i> Login</a>'
new_auth_block = '''<div class="nav-auth">
          <a href="login.html" class="btn-secondary" style="padding: 0.6rem 1.2rem; font-size: 0.9rem;"><i class="bi bi-person-circle"></i> Login</a>
          <a href="register.html" class="btn-primary" style="padding: 0.6rem 1.2rem; font-size: 0.9rem;"><i class="bi bi-person-plus"></i> Register</a>
        </div>'''

for fname in files_to_update:
    path = os.path.join(base_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if login_tag in content:
        content = content.replace(login_tag, new_auth_block)
        
    # Also fix index.html product images
    if fname == "index.html":
        # Replace the second instance of product-smartwatch.webp with product-smartwatch-elite.webp
        # and third with product-smartwatch-lite.webp
        
        parts = content.split('images/product-smartwatch.webp')
        # parts[0] + images/product-smartwatch.webp + parts[1] (Hero)
        # parts[1] + images/product-smartwatch.webp + parts[2] (Pro)
        # parts[2] + images/product-smartwatch.webp + parts[3] (Elite)
        # parts[3] + images/product-smartwatch.webp + parts[4] (Lite)
        
        if len(parts) >= 5:
            new_content = parts[0] + 'images/product-smartwatch.webp' + \
                          parts[1] + 'images/product-smartwatch.webp' + \
                          parts[2] + 'images/product-smartwatch-elite.webp' + \
                          parts[3] + 'images/product-smartwatch-lite.webp' + \
                          parts[4]
            content = new_content

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Files updated successfully!")
