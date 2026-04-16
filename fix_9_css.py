import re

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

# Read styles.css
with open(f"{base_dir}\styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# -------------------------------------------------------------
# 3. Checkerboard background bleeding
# -------------------------------------------------------------
css_append = """
/* Fix 3: Checkerboard Bleed */
#about {
    overflow: hidden !important;
}
@media (max-width: 768px) {
    #about {
        background-attachment: scroll !important;
    }
}

/* Fix 5: About Section Text Visibility */
.about-strip {
    background-color: #f1f5f9 !important; /* Slightly darker light theme for contrast */
}
.about-strip h3 {
    color: #c85a1a !important; /* Orange */
}
.about-strip p, .strip-text p {
    color: #1a2744 !important; /* Navy Blue */
}

/* Fix 6: Achievement Trophy Invisible (Assuming there's a class achievement-icon) */
.achievement-icon, .achievement-icon i, .trophy-icon, .trophy-icon i {
    color: #ffffff !important;
}
.achievement-card, .stat-card {
    position: relative;
    z-index: 1;
}

/* Fix 7: Course Cards Age/Duration Camouflage */
.course-meta, .course-info-bar, .card-meta {
    background-color: #f8f9fa !important;
    color: #1a2744 !important;
}
.course-meta i, .course-info-bar i, .card-meta i {
    color: #c85a1a !important;
}

/* Fix 8: Hero Section Mobile */
@media (max-width: 768px) {
    .hero.split-hero {
        display: flex !important;
        flex-direction: column !important; /* Stack image ABOVE text => wait, user prompt says:
        "Stacked layout where image appears as a full width block ABOVE the text content" */
    }
    .hero-right {
        order: -1 !important; /* Force image to top */
        height: 250px !important;
        display: block !important;
        width: 100% !important;
    }
    .hero-image-full {
        width: 100% !important;
        height: 250px !important;
        object-fit: cover !important;
        object-position: center top !important;
        position: relative !important;
    }
    .hero-left {
        order: 2 !important;
    }
}
"""

with open(f"{base_dir}\styles.css", "a", encoding="utf-8") as f:
    f.write(css_append)

print("CSS Fixes Appended")
