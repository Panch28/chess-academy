import re

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

with open(f"{base_dir}/index.html", "r", encoding="utf-8") as f:
    text = f.read()

# The user explicitly asked to "Delete the duplicate — keep only the one with the countdown timer."
# The one with the activity cards row that appears twice is the "activities-section".
text = re.sub(r'<div class="activities-section">.*?(?=</section>)', '', text, flags=re.DOTALL)

with open(f"{base_dir}/index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Duplicates removed.")
