import re
import os

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

# 1. HTML MODIFICATIONS (Why Choose Us, Stats Counter)
with open(f"{base_dir}/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix Stats Counter
# Replace <span class="stat-number" data-count="500">0</span> with just >500<
html = re.sub(r'<span class="stat-number" data-count="(\d+)">0</span>', r'<span class="stat-number-static">\1</span>', html)

# Fix Why Choose Us - reduce to exactly 3 cards.
# Wait, the prompt says they are repeating endlessly. Let's find the features-grid and keep only the first 3 items.
start_str = '<div class="features-grid">'
end_str = '</div>\n                </div>\n            </div>\n        </section>'

# Replace the inner contents of features-grid with just the first 3 feature items.
grid_items_replacement = """
                        <div class="feature-item">
                            <div class="feature-icon"><i class="fa-solid fa-user-graduate"></i></div>
                            <h4>Expert Coaches</h4>
                            <p>Learn from FIDE-rated players and certified coaches with proven track records.</p>
                        </div>
                        <div class="feature-item">
                            <div class="feature-icon"><i class="fa-solid fa-calendar-check"></i></div>
                            <h4>Flexible Schedule</h4>
                            <p>Weekend and weekday batches available to suit your child's routine.</p>
                        </div>
                        <div class="feature-item">
                            <div class="feature-icon"><i class="fa-solid fa-chart-line"></i></div>
                            <h4>Proven Methodology</h4>
                            <p>Structured curriculum from basics to advanced tournament preparation.</p>
                        </div>
"""
# Safe replacement using regex to find the start and end of features-grid
html = re.sub(r'<div class="features-grid">.*?</div>\s*</div>\s*</div>\s*</section>', 
              f'<div class="features-grid">{grid_items_replacement}</div>\n                </div>\n            </div>\n        </section>', 
              html, flags=re.DOTALL)


with open(f"{base_dir}/index.html", "w", encoding="utf-8") as f:
    f.write(html)

# 2. JS MODIFICATIONS (Remove Counter Animation)
with open(f"{base_dir}/script.js", "r", encoding="utf-8") as f:
    js = f.read()

# Just comment out the updateCounter execution to prevent it doing anything.
js = js.replace('const statItems = entry.target.querySelectorAll(\'.stat-number\');\n                statItems.forEach(stat => animateCounter(stat));', 
               '// Animation removed per user request')

with open(f"{base_dir}/script.js", "w", encoding="utf-8") as f:
    f.write(js)

# 3. CSS MODIFICATIONS (About Background, Hero Image)
css_fixes = """
/* ==========================================================================
   4 SPECIFIC FIXES REQUESTED
   ========================================================================== */

/* 1. About section background fix */
.about-war-room, .about-bg-elements, .about-board-texture, .about-noise {
    background-image: none !important;
}
.about-war-room {
    background-color: #1B2F5E !important;
}
.about-war-room *, .about-war-room h2, .about-war-room h3, .about-war-room p {
    color: #FFFFFF !important;
}

/* 2. Hero Image resize fix */
.hero-right {
    position: relative !important;
    overflow: hidden !important;
}

.hero-image-full {
    position: absolute !important; /* Ensure children don't overflow by being block level */
    top: 0;
    left: 0;
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    object-position: center top !important;
}

/* Let's clear the old mobile absolute/relative confusion for hero-image-full */
@media (max-width: 992px) {
    .hero-image-full {
        position: absolute !important;
        width: 100% !important;
        height: 100% !important;
    }
}
"""

with open(f"{base_dir}/styles.css", "a", encoding="utf-8") as f:
    f.write(css_fixes)

print("4 Fixes Applied")
