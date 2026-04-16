import re

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

# Fix HTML
with open(f"{base_dir}/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Nuke the entire div for drag hint
html = re.sub(r'<div class="gallery-drag-hint-3d">.*?</div>', '', html, flags=re.DOTALL)
with open(f"{base_dir}/index.html", "w", encoding="utf-8") as f:
    f.write(html)

# Fix CSS
with open(f"{base_dir}/styles.css", "a", encoding="utf-8") as f:
    f.write("""
/* GALLERY ULTIMATE HEIGHT FIX */
.circular-gallery-wrapper {
    display: block !important;
    height: auto !important;
    min-height: 350px !important;
    position: relative !important;
    padding: 0 40px !important; /* give room for the arrow buttons */
}
#galleryTrack {
    align-items: stretch !important;
    height: 300px !important;
    padding: 25px !important;
}
.gallery-item-3d {
    height: 100% !important; /* Fill the track height */
    min-height: 250px !important;
}
.gallery-nav-btn {
    top: 50% !important;
    transform: translateY(-50%) !important;
    z-index: 100 !important;
}
.gallery-nav-btn.prev {
    left: 0 !important;
}
.gallery-nav-btn.next {
    right: 0 !important;
}
""")
print("Gallery definitively fixed.")
