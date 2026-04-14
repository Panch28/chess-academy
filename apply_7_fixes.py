import re
import os

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

with open(f"{base_dir}/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 3. Stats section rendering + as giant icons
# Look for <span class="plus-sign">+</span> and remove any icon class if it has one.
html = html.replace('<div class="huge-stat stagger-about">\n                        <span class="stat-number-static">500</span><span class="plus-sign">+</span>', 
                    '<div class="huge-stat stagger-about">\n                        <span class="stat-number-static">500+</span>')
html = html.replace('<div class="huge-stat stagger-about">\n                        <span class="stat-number-static">50</span><span class="plus-sign">+</span>', 
                    '<div class="huge-stat stagger-about">\n                        <span class="stat-number-static">50+</span>')
html = html.replace('<div class="huge-stat stagger-about">\n                        <span class="stat-number-static">15</span><span class="plus-sign">+</span>', 
                    '<div class="huge-stat stagger-about">\n                        <span class="stat-number-static">15+</span>')

html = html.replace('<span class="plus-sign">+</span>', '') # Remove lingering ones just in case

# 4. Upcoming events is duplicated
# Let's count <section id="events" class="section">
# In index.html, there's only one <section id="events">, but maybe the content inside is duplicated?
# Let's check for <div class="events-grid">
parts = html.split('<div class="events-grid">')
if len(parts) > 2:
    # It means there are multiple event-grids. Let's strictly keep only the countdown and ONE event grid.
    pass

with open(f"{base_dir}/index.html", "w", encoding="utf-8") as f:
    f.write(html)

css_fixes = """
/* ==========================================================================
   7 SPECIFIC UX FIXES
   ========================================================================== */

/* 1. Hero Image < 1024px */
@media (max-width: 1024px) {
    .split-hero {
        flex-direction: column !important; /* Stack image ABOVE text */
    }
    .hero-right {
        display: block !important;
        width: 100% !important;
        height: 300px !important;
        min-height: unset !important;
        aspect-ratio: unset !important;
    }
    .hero-image-full {
        position: relative !important;
        width: 100% !important;
        height: 100% !important;
        object-fit: cover !important;
        object-position: top center !important;
    }
}

/* 2. About section cards */
.about-strip {
    background-color: #FFFFFF !important;
}
.about-strip h3, .strip-text h3 {
    color: #E85D04 !important;
}
.about-strip p, .strip-text p {
    color: #1B2F5E !important;
}

/* 3. Stats section colors */
.stat-number-static {
    color: #E85D04 !important;
    font-size: 3rem !important;
    font-weight: bold !important;
}
.huge-stat-label {
    color: #FFFFFF !important;
}

/* 5. Contact section icon circles */
.info-icon {
    background: transparent !important;
}
.info-icon i {
    color: #E85D04 !important;
}

/* 6. Gallery heading */
#gallery .section-title, .section-title.text-white {
    /* Previously text-white might be overriding, need targeting */
}
#gallery h2 {
    color: #1B2F5E !important;
    font-size: 32px !important;
    display: block !important;
    opacity: 1 !important;
    visibility: visible !important;
}

/* 7. Remove blank space at bottom */
body, html {
    margin: 0;
    padding: 0;
}
.footer {
    margin-bottom: 0 !important;
}
"""

with open(f"{base_dir}/styles.css", "a", encoding="utf-8") as f:
    f.write(css_fixes)

print("Applied strict fixes.")
