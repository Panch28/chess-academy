import re
import os

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

# 1. HTML
with open(f"{base_dir}/index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = re.sub(r'<p class=\"text-center text-primary.*?>.*?Explore.*?our.*?moments.*?</p>', '', html, flags=re.DOTALL | re.IGNORECASE)
html = re.sub(r'<p class=\"text-center text-primary.*?>.*?Drag.*?or.*?scroll.*?</p>', '', html, flags=re.DOTALL | re.IGNORECASE)
html = html.replace("Drag or scroll to explore our moments", "")

with open(f"{base_dir}/index.html", "w", encoding="utf-8") as f:
    f.write(html)


# 2. JS
with open(f"{base_dir}/script.js", "r", encoding="utf-8") as f:
    js = f.read()

# Neutering init3DGallery
# We will replace everything inside init3DGallery so it doesn't initialize the canvas scroll hacking, 
# but simply handles native CSS slider arrows.
# I'll replace the old init3DGallery completely.

new_init = """
function init3DGallery() {
    const track = document.getElementById('galleryTrack');
    const prevBtn = document.getElementById('galleryPrev');
    const nextBtn = document.getElementById('galleryNext');
    if (!track) return;
    
    // Nuke old canvas if it exists
    const oldCanvas = track.querySelector('canvas');
    if (oldCanvas) oldCanvas.remove();

    if (prevBtn) {
        prevBtn.onclick = () => {
            track.scrollBy({ left: -300, behavior: 'smooth' });
        };
    }
    if (nextBtn) {
        nextBtn.onclick = () => {
            track.scrollBy({ left: 300, behavior: 'smooth' });
        };
    }
}
window.init3DGallery = init3DGallery;
"""

# Replace the giant init3DGallery loop in script.js
js = re.sub(r'function init3DGallery\(\) \{.*?(?=// Testimonial Slider)', new_init + '\n\n', js, flags=re.DOTALL)

with open(f"{base_dir}/script.js", "w", encoding="utf-8") as f:
    f.write(js)

# 3. CSS
with open(f"{base_dir}/styles.css", "a", encoding="utf-8") as f:
    f.write("""
/* ==========================================================================
   NATIVE CSS GALLERY FIX
   ========================================================================== */
.gallery-container {
    padding-bottom: 20px !important;
    position: relative !important;
}

#galleryTrack {
    display: flex !important;
    overflow-x: auto !important;
    scroll-snap-type: x mandatory !important;
    scroll-behavior: smooth !important;
    gap: 20px !important;
    padding: 20px !important;
    margin: 0 !important;
    position: static !important;
    height: auto !important;
    perspective: none !important;
    -webkit-overflow-scrolling: touch !important;
}
#galleryTrack::-webkit-scrollbar {
    height: 8px !important;
}
#galleryTrack::-webkit-scrollbar-thumb {
    background-color: #c85a1a !important;
    border-radius: 4px !important;
}

.gallery-item-3d {
    flex: 0 0 calc(100% - 40px) !important;
    max-width: 350px !important;
    min-width: 250px !important;
    height: 250px !important;
    position: relative !important;
    scroll-snap-align: center !important;
    transform: none !important;
    opacity: 1 !important;
    display: block !important;
    border-radius: 15px !important;
    overflow: hidden !important;
    box-shadow: 0 10px 20px rgba(0,0,0,0.1) !important;
}

.gallery-item-3d img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    display: block !important;
}

.gallery-item-3d .item-overlay {
    background: linear-gradient(to top, rgba(26, 39, 68, 0.9), transparent) !important;
}
.gallery-item-3d .item-label {
    position: absolute !important;
    bottom: 20px !important;
    left: 0 !important;
    width: 100% !important;
    text-align: center !important;
    color: #ffffff !important;
    font-size: 1.2rem !important;
    font-weight: bold !important;
}

/* Nuke the canvas completely */
#galleryTrack canvas {
    display: none !important;
}
""")

print("Gallery removed 3D canvas and converted to native sliding CSS.")
