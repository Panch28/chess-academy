import re

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

# 1. Restore complete Section HTML perfectly
with open(f"{base_dir}/old_index.html", "r", encoding="utf-16") as f:
    old_html = f.read()

old_section_match = re.search(r'(<section id="gallery".*?</section>)', old_html, re.DOTALL | re.IGNORECASE)
if old_section_match:
    perfect_gall = old_section_match.group(1)
    # Remove hints
    perfect_gall = re.sub(r'<div class="gallery-drag-hint-3d">.*?</div>', '', perfect_gall, flags=re.DOTALL)
    perfect_gall = re.sub(r'<p class="text-center text-primary.*?>.*?Explore.*?our.*?moments.*?</p>', '', perfect_gall, flags=re.DOTALL | re.IGNORECASE)

    with open(f"{base_dir}/index.html", "r", encoding="utf-8") as f:
        curr_html = f.read()
    curr_html = re.sub(r'<section id="gallery".*?</section>', perfect_gall, curr_html, flags=re.DOTALL | re.IGNORECASE)
    with open(f"{base_dir}/index.html", "w", encoding="utf-8") as f:
        f.write(curr_html)

# 2. Fix multiple init3DGallery invocations in script.js
with open(f"{base_dir}/script.js", "r", encoding="utf-8") as f:
    js = f.read()

# Make it single-run for events
new_init = """function init3DGallery() {
    const wrapper = document.getElementById('circularGallery');
    const track = document.getElementById('galleryTrack');
    const centerLabel = document.getElementById('centerLabel');
    const prevBtn = document.getElementById('galleryPrev');
    const nextBtn = document.getElementById('galleryNext');
    if (!wrapper || !track) return;
    
    // Only bind events and loops ONCE
    if (window._galleryInitialized) {
        // Just force an update
        if (window._updateGallery) window._updateGallery();
        return;
    }
    window._galleryInitialized = true;

    let currentScroll = 0;
    let targetScroll = 0;
    let velocity = 0;
    let isDragging = false;
    let lastX = 0;
    let animationId = null;
    let autoPlayTimer = null;
    let autoplayPaused = false;
    
    function startAutoplay() {
        if(autoPlayTimer) clearInterval(autoPlayTimer);
        autoPlayTimer = setInterval(() => {
            if(!autoplayPaused) {
                targetScroll += getSpacing();
            }
        }, 4000);
    }
    function resetAutoplay() { startAutoplay(); }
    function getSpacing() { return window.innerWidth <= 768 ? window.innerWidth * 0.75 + 15 : 440; }

    window._updateGallery = function updateGallery() {
        const items = track.querySelectorAll('.gallery-item-3d');
        if (items.length === 0) return;
        
        const spacing = getSpacing();
        const maxScroll = (items.length - 1) * spacing;
        
        if(currentScroll > maxScroll + spacing) {
            currentScroll = 0;
            targetScroll = 0;
        }

        let centerIndex = Math.round(currentScroll / spacing);
        centerIndex = Math.max(0, Math.min(centerIndex, items.length - 1));
        
        if (items[centerIndex]) {
            const lbl = items[centerIndex].querySelector('.item-label');
            if(lbl && centerLabel) {
                centerLabel.textContent = lbl.textContent;
                centerLabel.classList.add('active');
            }
        }
        
        items.forEach((item, index) => {
            const distance = (index * spacing) - currentScroll;
            const diffRatio = distance / spacing;
            const x = distance;
            
            const absRatio = Math.abs(diffRatio);
            const rotateY = diffRatio * -25;
            const translateZ = absRatio * -100;
            let scale = 1 - Math.min(0.3, absRatio * 0.2); 
            const opacity = Math.max(0, 1 - absRatio * 0.5); 
            const zIndex = 100 - Math.round(absRatio * 10);
            
            if (item.matches(':hover') && absRatio < 0.2) scale += 0.03;
            
            item.style.transform = `translateX(${x}px) translateZ(${translateZ}px) rotateY(${rotateY}deg) scale(${scale})`;
            item.style.opacity = opacity;
            item.style.zIndex = zIndex;
            
            const img = item.querySelector('img');
            if (img) {
                if (absRatio < 0.2) img.style.filter = 'grayscale(0%) saturate(120%)';
                else img.style.filter = 'grayscale(100%)';
            }
        });
    }

    function animate() {
        if (!isDragging) {
            velocity *= 0.9;
            currentScroll += (targetScroll - currentScroll) * 0.1;
        } else {
            currentScroll = targetScroll;
        }
        
        const spacing = getSpacing();
        const items = track.querySelectorAll('.gallery-item-3d');
        const maxScroll = Math.max(0, (items.length - 1) * spacing);
        if(currentScroll < -spacing/2) currentScroll = targetScroll = -spacing/2;
        
        window._updateGallery();
        animationId = requestAnimationFrame(animate);
    }
    
    function snapToNearest() {
        const spacing = getSpacing();
        const items = track.querySelectorAll('.gallery-item-3d');
        let nearestIndex = Math.round(targetScroll / spacing);
        nearestIndex = Math.max(0, Math.min(nearestIndex, items.length - 1));
        targetScroll = nearestIndex * spacing;
    }

    wrapper.addEventListener('mousedown', (e) => {
        isDragging = true; autoplayPaused = true;
        lastX = e.clientX; wrapper.style.cursor = 'grabbing';
    });
    window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        targetScroll -= (e.clientX - lastX) * 1.5;
        lastX = e.clientX;
    });
    window.addEventListener('mouseup', () => {
        if (!isDragging) return;
        isDragging = false; wrapper.style.cursor = 'grab';
        snapToNearest(); autoplayPaused = false; resetAutoplay();
    });
    
    wrapper.addEventListener('touchstart', (e) => {
        isDragging = true; autoplayPaused = true; lastX = e.touches[0].clientX;
    }, {passive: true});
    window.addEventListener('touchmove', (e) => {
        if (!isDragging) return;
        targetScroll -= (e.touches[0].clientX - lastX) * 1.5;
        lastX = e.touches[0].clientX;
    });
    window.addEventListener('touchend', () => {
        if (!isDragging) return;
        isDragging = false; snapToNearest(); autoplayPaused = false; resetAutoplay();
    });

    wrapper.addEventListener('mouseenter', () => autoplayPaused = true);
    wrapper.addEventListener('mouseleave', () => {
        if(!isDragging) autoplayPaused = false;
        targetScroll = currentScroll; 
    });

    if (prevBtn) prevBtn.addEventListener('click', () => { targetScroll -= getSpacing(); snapToNearest(); });
    if (nextBtn) nextBtn.addEventListener('click', () => { targetScroll += getSpacing(); snapToNearest(); });

    wrapper.style.cursor = 'grab';
    startAutoplay();
    animate();
}
"""

start_curr = js.find('function init3DGallery()')
if start_curr != -1:
    brace_count, in_func, end_curr = 0, False, start_curr
    for i in range(start_curr, len(js)):
        if js[i] == '{':
            if not in_func: in_func = True
            brace_count += 1
        elif js[i] == '}':
            brace_count -= 1
            if in_func and brace_count == 0:
                end_curr = i + 1
                break
    js = js[:start_curr] + new_init + js[end_curr:]
    with open(f"{base_dir}/script.js", "w", encoding="utf-8") as f:
        f.write(js)

print("Perfectly restored HTML block and disabled double event registration")
