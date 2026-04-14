import re

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

with open(f"{base_dir}/script.js", "r", encoding="utf-8") as f:
    js = f.read()

# 1. Remove the preloader fetch and error-prone timeout block, letting animations run instantly
js = re.sub(
    r'const preloader = document.getElementById\(\'preloader\'\);\s+const navbar',
    'const navbar',
    js
)

js = re.sub(
    r'setTimeout\(\(\) => \{\s+preloader\.classList\.add\(\'hidden\'\);\s+(.*?)\}\s*,\s*2200\);',
    r'\1',
    js,
    flags=re.DOTALL
)

with open(f"{base_dir}/script.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Script.js fixed.")
