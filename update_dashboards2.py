import os
import re

def update_file(filename, dashboard_link, is_admin=False):
    if not os.path.exists(filename):
        return
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. Update logos to be clickable
    # Sidebar logo
    content = content.replace(
        '<div class="sidebar-header">',
        f'<a href="{dashboard_link}" class="sidebar-header" style="text-decoration: none;">'
    ).replace(
        '<span>STACKLY</span>\n    </div>',
        '<span>STACKLY</span>\n    </a>'
    )
    
    # Mobile logo
    content = content.replace(
        '<div class="mobile-logo">',
        f'<a href="{dashboard_link}" class="mobile-logo" style="text-decoration: none;">'
    ).replace(
        '<span>STACKLY</span>\n    </div>',
        '<span>STACKLY</span>\n    </a>'
    )
    
    # 2. Add images to dashboards
    if filename == 'admin-dashboard.html':
        banner = """
    <!-- Promotional Banner with Image -->
    <div class="glass-card" style="margin-bottom: 2rem; overflow: hidden; position: relative; padding: 2rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; background: linear-gradient(135deg, rgba(0,180,216,0.05), rgba(123,47,247,0.05)); border-left: 4px solid var(--primary-color);">
      <div style="flex: 1; min-width: 250px;">
        <h2 style="font-family: 'Orbitron', sans-serif; margin-bottom: 0.5rem; font-size: 1.5rem;">Stackly Vision Enterprise Released</h2>
        <p style="color: var(--text-muted); margin-bottom: 1rem;">Check out the latest sales and activation metrics for our newest enterprise AR glasses.</p>
        <a href="admin-devices.html" class="btn-primary" style="padding: 0.5rem 1rem; border-radius: 8px; font-size: 0.85rem; text-decoration: none;">View Devices</a>
      </div>
      <img src="images/product-arglasses.webp" alt="AR Glasses" style="height: 120px; object-fit: contain; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.3));">
    </div>
    """
        content = content.replace('<div class="kpi-grid">', banner + '\n    <div class="kpi-grid">')
        
    elif filename == 'admin-users.html':
        content = content.replace(
            '<div class="user-card-avatar" style="width: 32px; height: 32px; min-width: 32px; font-size: 0.7rem;">SM</div>',
            '<img src="images/team-1.webp" class="user-card-avatar" style="width: 32px; height: 32px; min-width: 32px; object-fit: cover;">'
        ).replace(
            '<div class="user-card-avatar" style="width: 32px; height: 32px; min-width: 32px; font-size: 0.7rem;">JC</div>',
            '<img src="images/team-2.webp" class="user-card-avatar" style="width: 32px; height: 32px; min-width: 32px; object-fit: cover;">'
        ).replace(
            '<div class="user-card-avatar" style="width: 32px; height: 32px; min-width: 32px; font-size: 0.7rem;">AP</div>',
            '<img src="images/team-3.webp" class="user-card-avatar" style="width: 32px; height: 32px; min-width: 32px; object-fit: cover;">'
        ).replace(
            '<div class="user-card-avatar" style="width: 32px; height: 32px; min-width: 32px; font-size: 0.7rem; background: #333;">MJ</div>',
            '<img src="images/blog-1.webp" class="user-card-avatar" style="width: 32px; height: 32px; min-width: 32px; object-fit: cover;">'
        ).replace(
            '<div class="user-card-avatar" style="width: 32px; height: 32px; min-width: 32px; font-size: 0.7rem;">LW</div>',
            '<img src="images/blog-2.webp" class="user-card-avatar" style="width: 32px; height: 32px; min-width: 32px; object-fit: cover;">'
        )
        
    elif filename == 'admin-devices.html':
        content = content.replace(
            '<div class="user-card-avatar" style="background: rgba(0,180,216,0.2);"><i class="bi bi-smartwatch" style="color: var(--primary-color); font-size: 1.5rem;"></i></div>',
            '<div class="user-card-avatar" style="background: transparent;"><img src="images/product-smartwatch.webp" style="width: 100%; height: 100%; object-fit: contain; padding: 2px;"></div>'
        ).replace(
            '<div class="user-card-avatar" style="background: rgba(123,47,247,0.2);"><i class="bi bi-watch" style="color: var(--secondary-color); font-size: 1.5rem;"></i></div>',
            '<div class="user-card-avatar" style="background: transparent;"><img src="images/product-fitness.webp" style="width: 100%; height: 100%; object-fit: contain; padding: 2px;"></div>'
        ).replace(
            '<div class="user-card-avatar" style="background: rgba(0,245,160,0.2);"><i class="bi bi-eyeglasses" style="color: var(--accent-green); font-size: 1.5rem;"></i></div>',
            '<div class="user-card-avatar" style="background: transparent;"><img src="images/product-arglasses.webp" style="width: 100%; height: 100%; object-fit: contain; padding: 2px;"></div>'
        ).replace(
            '<div class="user-card-avatar" style="background: rgba(255,51,102,0.2);"><i class="bi bi-smartwatch" style="color: var(--accent-pink); font-size: 1.5rem;"></i></div>',
            '<div class="user-card-avatar" style="background: transparent;"><img src="images/product-smartwatch-lite.webp" style="width: 100%; height: 100%; object-fit: contain; padding: 2px;"></div>'
        )

    elif filename == 'user-dashboard.html':
        content = content.replace(
            '<div class="device-img"><i class="bi bi-smartwatch"></i></div>',
            '<div class="device-img" style="background: transparent;"><img src="images/product-smartwatch-elite.webp" style="width: 100%; height: 100%; object-fit: contain;"></div>'
        ).replace(
            '<div class="device-img"><i class="bi bi-watch"></i></div>',
            '<div class="device-img" style="background: transparent;"><img src="images/product-fitness.webp" style="width: 100%; height: 100%; object-fit: contain;"></div>'
        )
        
    elif filename == 'developer-dashboard.html':
        banner = """
    <!-- Dev Banner with Image -->
    <div class="glass-card" style="margin-bottom: 2rem; overflow: hidden; position: relative; padding: 2rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; background: linear-gradient(135deg, rgba(123,47,247,0.05), rgba(0,180,216,0.05)); border-left: 4px solid var(--secondary-color);">
      <div style="flex: 1; min-width: 250px;">
        <h2 style="font-family: 'Orbitron', sans-serif; margin-bottom: 0.5rem; font-size: 1.5rem;">Developer Tools v4.0</h2>
        <p style="color: var(--text-muted); margin-bottom: 1rem;">Access the newest health sensors and real-time streaming APIs for the Stackly Watch Pro.</p>
        <a href="error.html" class="btn-primary" style="padding: 0.5rem 1rem; border-radius: 8px; font-size: 0.85rem; text-decoration: none;"><i class="bi bi-journal-code"></i> Read Docs</a>
      </div>
      <img src="images/service-dev.webp" alt="Developer Tools" style="height: 120px; border-radius: 8px; object-fit: cover; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.3));">
    </div>
    """
        content = content.replace('<div class="api-grid">', banner + '\n    <div class="api-grid">')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

update_file('admin-dashboard.html', 'admin-dashboard.html', True)
update_file('admin-users.html', 'admin-dashboard.html', True)
update_file('admin-devices.html', 'admin-dashboard.html', True)
update_file('user-dashboard.html', 'user-dashboard.html', False)
update_file('developer-dashboard.html', 'developer-dashboard.html', False)
