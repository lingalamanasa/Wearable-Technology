import os
import re

with open('admin-dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# For admin-users.html
users_content = content.replace(
    '<a href="admin-dashboard.html" class="active">', '<a href="admin-dashboard.html">'
).replace(
    '<a href="admin-users.html">', '<a href="admin-users.html" class="active">'
).replace(
    '<h1>Admin <span>Dashboard</span></h1>', '<h1>Admin <span>Users</span></h1>'
)

users_main = """
    <!-- Users Stats -->
    <div class="kpi-grid">
      <div class="glass-card kpi-card">
        <div class="kpi-icon cyan"><i class="bi bi-people-fill"></i></div>
        <div class="kpi-info">
          <h3>12,847</h3>
          <p>Total Users</p>
        </div>
      </div>
      <div class="glass-card kpi-card">
        <div class="kpi-icon green"><i class="bi bi-person-check-fill"></i></div>
        <div class="kpi-info">
          <h3>10,240</h3>
          <p>Active (30d)</p>
        </div>
      </div>
      <div class="glass-card kpi-card">
        <div class="kpi-icon purple"><i class="bi bi-star-fill"></i></div>
        <div class="kpi-info">
          <h3>4,521</h3>
          <p>Premium Subs</p>
        </div>
      </div>
    </div>

    <!-- User Directory -->
    <div class="glass-card table-card">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
        <h3>User Directory</h3>
        <div style="display: flex; gap: 1rem;">
          <input type="text" placeholder="Search users..." style="padding: 0.5rem 1rem; border-radius: 8px; border: 1px solid var(--border-color); background: rgba(0,0,0,0.2); color: #fff;">
          <button class="btn-primary" style="padding: 0.5rem 1rem; border-radius: 8px;"><i class="bi bi-filter"></i> Filter</button>
        </div>
      </div>
      <div style="overflow-x: auto;">
        <table class="dash-table">
          <thead><tr><th>User</th><th>Email</th><th>Role</th><th>Status</th><th>Last Login</th><th>Actions</th></tr></thead>
          <tbody>
            <tr>
              <td style="display: flex; align-items: center; gap: 0.8rem;">
                <div class="user-card-avatar" style="width: 32px; height: 32px; min-width: 32px; font-size: 0.7rem;">SM</div>
                Sarah Mitchell
              </td>
              <td>sarah.m@example.com</td>
              <td>Premium</td>
              <td><span class="status-badge active">Active</span></td>
              <td>2 hours ago</td>
              <td><button style="background: none; border: none; color: var(--text-muted); cursor: pointer;"><i class="bi bi-three-dots-vertical"></i></button></td>
            </tr>
            <tr>
              <td style="display: flex; align-items: center; gap: 0.8rem;">
                <div class="user-card-avatar" style="width: 32px; height: 32px; min-width: 32px; font-size: 0.7rem;">JC</div>
                James Chen
              </td>
              <td>james.c@example.com</td>
              <td>Enterprise</td>
              <td><span class="status-badge active">Active</span></td>
              <td>5 hours ago</td>
              <td><button style="background: none; border: none; color: var(--text-muted); cursor: pointer;"><i class="bi bi-three-dots-vertical"></i></button></td>
            </tr>
            <tr>
              <td style="display: flex; align-items: center; gap: 0.8rem;">
                <div class="user-card-avatar" style="width: 32px; height: 32px; min-width: 32px; font-size: 0.7rem;">AP</div>
                Anika Patel
              </td>
              <td>anika.p@example.com</td>
              <td>Developer</td>
              <td><span class="status-badge active">Active</span></td>
              <td>1 day ago</td>
              <td><button style="background: none; border: none; color: var(--text-muted); cursor: pointer;"><i class="bi bi-three-dots-vertical"></i></button></td>
            </tr>
            <tr>
              <td style="display: flex; align-items: center; gap: 0.8rem;">
                <div class="user-card-avatar" style="width: 32px; height: 32px; min-width: 32px; font-size: 0.7rem; background: #333;">MJ</div>
                Mike Johnson
              </td>
              <td>mike.j@example.com</td>
              <td>Starter</td>
              <td><span class="status-badge inactive">Inactive</span></td>
              <td>3 weeks ago</td>
              <td><button style="background: none; border: none; color: var(--text-muted); cursor: pointer;"><i class="bi bi-three-dots-vertical"></i></button></td>
            </tr>
            <tr>
              <td style="display: flex; align-items: center; gap: 0.8rem;">
                <div class="user-card-avatar" style="width: 32px; height: 32px; min-width: 32px; font-size: 0.7rem;">LW</div>
                Lisa Wang
              </td>
              <td>lisa.w@example.com</td>
              <td>Premium</td>
              <td><span class="status-badge active">Active</span></td>
              <td>1 hour ago</td>
              <td><button style="background: none; border: none; color: var(--text-muted); cursor: pointer;"><i class="bi bi-three-dots-vertical"></i></button></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
"""

header_match = re.search(r'(<div class="dash-header">.*?</div>)', users_content, re.DOTALL)
if header_match:
    header = header_match.group(1)
    main_pattern = r'<main class="main-content">.*?</main>'
    new_main = f'<main class="main-content">\n    {header}\n{users_main}\n  </main>'
    users_content = re.sub(main_pattern, new_main, users_content, flags=re.DOTALL)

with open('admin-users.html', 'w', encoding='utf-8') as f:
    f.write(users_content)


# For admin-devices.html
devices_content = content.replace(
    '<a href="admin-dashboard.html" class="active">', '<a href="admin-dashboard.html">'
).replace(
    '<a href="admin-devices.html">', '<a href="admin-devices.html" class="active">'
).replace(
    '<h1>Admin <span>Dashboard</span></h1>', '<h1>Admin <span>Devices</span></h1>'
)

devices_main = """
    <!-- Device Stats -->
    <div class="kpi-grid">
      <div class="glass-card kpi-card">
        <div class="kpi-icon green"><i class="bi bi-smartwatch"></i></div>
        <div class="kpi-info">
          <h3>8,392</h3>
          <p>Active Devices</p>
        </div>
      </div>
      <div class="glass-card kpi-card">
        <div class="kpi-icon cyan"><i class="bi bi-arrow-repeat"></i></div>
        <div class="kpi-info">
          <h3>1,204</h3>
          <p>Syncing Now</p>
        </div>
      </div>
      <div class="glass-card kpi-card">
        <div class="kpi-icon pink"><i class="bi bi-exclamation-triangle"></i></div>
        <div class="kpi-info">
          <h3>18</h3>
          <p>Errors (24h)</p>
        </div>
      </div>
    </div>

    <!-- Device Inventory -->
    <h3 style="font-family: 'Outfit', sans-serif; font-size: 1.1rem; margin-bottom: 1rem; font-weight: 700;">Device Inventory</h3>
    <div class="users-grid">
      <div class="glass-card user-card">
        <div class="user-card-avatar" style="background: rgba(0,180,216,0.2);"><i class="bi bi-smartwatch" style="color: var(--primary-color); font-size: 1.5rem;"></i></div>
        <div class="user-card-info"><h4>Watch Pro v3</h4><p>4,210 Active • FW v2.4</p></div>
        <div class="user-card-actions"><button title="Manage"><i class="bi bi-gear"></i></button></div>
      </div>
      <div class="glass-card user-card">
        <div class="user-card-avatar" style="background: rgba(123,47,247,0.2);"><i class="bi bi-watch" style="color: var(--secondary-color); font-size: 1.5rem;"></i></div>
        <div class="user-card-info"><h4>Band X</h4><p>3,105 Active • FW v1.2</p></div>
        <div class="user-card-actions"><button title="Manage"><i class="bi bi-gear"></i></button></div>
      </div>
      <div class="glass-card user-card">
        <div class="user-card-avatar" style="background: rgba(0,245,160,0.2);"><i class="bi bi-eyeglasses" style="color: var(--accent-green); font-size: 1.5rem;"></i></div>
        <div class="user-card-info"><h4>Vision Enterprise</h4><p>850 Active • FW v3.0</p></div>
        <div class="user-card-actions"><button title="Manage"><i class="bi bi-gear"></i></button></div>
      </div>
      <div class="glass-card user-card">
        <div class="user-card-avatar" style="background: rgba(255,51,102,0.2);"><i class="bi bi-smartwatch" style="color: var(--accent-pink); font-size: 1.5rem;"></i></div>
        <div class="user-card-info"><h4>Watch Lite</h4><p>227 Active • FW v1.0</p></div>
        <div class="user-card-actions"><button title="Manage"><i class="bi bi-gear"></i></button></div>
      </div>
    </div>
    
    <!-- Global Map Placeholder -->
    <div class="glass-card chart-card" style="margin-top: 2rem;">
      <h3>Global Device Distribution</h3>
      <div class="chart-placeholder" style="height: 300px;"><i class="bi bi-globe" style="font-size: 3rem;"></i><p>Interactive Map Visualization</p></div>
    </div>
"""

header_match2 = re.search(r'(<div class="dash-header">.*?</div>)', devices_content, re.DOTALL)
if header_match2:
    header2 = header_match2.group(1)
    new_main2 = f'<main class="main-content">\n    {header2}\n{devices_main}\n  </main>'
    devices_content = re.sub(main_pattern, new_main2, devices_content, flags=re.DOTALL)

with open('admin-devices.html', 'w', encoding='utf-8') as f:
    f.write(devices_content)
