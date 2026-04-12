import re

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

with open(f"{base_dir}/admin.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add Favicon if not exist
if "favicon.ico" not in html:
    html = html.replace("</title>", "</title>\n  <link rel=\"icon\" type=\"image/x-icon\" href=\"favicon.ico\">")

# Replace Login Screen Logo
html = re.sub(
    r'<div class="logo"><i class="fa-solid fa-chess-knight"></i> Sri Sai Chess Academy</div>',
    '<div class="logo"><img src="logo.png" style="height: 48px; width: auto;" alt="Logo"> Sri Sai Chess Academy</div>',
    html
)

# Replace Dashboard Topbar Logo
html = re.sub(
    r'<div class="topbar-logo"><i class="fa-solid fa-chess-knight"></i> Admin Panel</div>',
    '<div class="topbar-logo" style="display:flex;align-items:center;gap:10px;"><img src="logo.png" style="height: 38px; width: auto;" alt="Logo"> Admin Panel</div>',
    html
)

with open(f"{base_dir}/admin.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Admin logos updated.")
