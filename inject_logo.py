import re

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

with open(f"{base_dir}/index.html", "r", encoding="utf-8") as f:
    curr_html = f.read()

# 1. Add Favicon
if "favicon.ico" not in curr_html:
    curr_html = curr_html.replace("</title>", "</title>\n    <link rel=\"icon\" type=\"image/x-icon\" href=\"favicon.ico\">")

# 2. Replace the navbar logo
curr_html = re.sub(
    r'<div class="logo">.*?</div>',
    '<div class="logo">\n              <img src="logo.png" alt="Sri Sai Chess Academy Logo">\n          </div>',
    curr_html,
    flags=re.DOTALL
)

with open(f"{base_dir}/index.html", "w", encoding="utf-8") as f:
    f.write(curr_html)

# Add CSS for .logo img
with open(f"{base_dir}/styles.css", "a", encoding="utf-8") as f:
    f.write("""
/* LOGO FIX */
.logo {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
}
.logo img {
    height: 48px;
    width: auto;
    object-fit: contain;
}
@media (max-width: 768px) {
    .logo img {
        height: 38px;
    }
}
""")
print("Injected logo into HTML and CSS!")
