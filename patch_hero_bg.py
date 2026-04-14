import re

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

with open(f"{base_dir}\styles.css", "a", encoding="utf-8") as f:
    f.write("""
/* ==========================================================================
   MOBILE FULL-SCREEN BACKGROUND HERO (PER NEW PROMPT)
   ========================================================================== */

@media (max-width: 992px) {
    /* 1. Make the hero 100vh height and stack everything inside */
    .hero.split-hero {
        display: block !important;
        position: relative !important;
        width: 100% !important;
        min-height: 100vh !important;
        height: auto !important;
        margin: 0 !important;
        padding: 0 !important;
        border-radius: 0 !important;
        background-color: #1a2744 !important; /* Navy Blue fallback */
    }

    /* 2. Convert right column to an absolute background layer */
    .hero-right {
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 100% !important;
        display: block !important;
        z-index: 1 !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* 3. Image perfectly fills as cover and stays centered */
    .hero-image-full {
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 100% !important;
        object-fit: cover !important;
        object-position: center !important;
        z-index: 1 !important;
        display: block !important;
    }

    /* 4. Overlay to make text readable (navy blue tint) */
    .hero-right::after {
        content: '' !important;
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 100% !important;
        background: linear-gradient(to bottom, rgba(26, 39, 68, 0.6), rgba(26, 39, 68, 0.9)) !important; /* Navy blue overlay */
        z-index: 2 !important;
    }

    /* 5. Left column stays on top with centered content */
    .hero-left {
        position: relative !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        min-height: 100vh !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        background-color: transparent !important;
        z-index: 10 !important;
        padding: 40px 20px !important;
    }

    /* Make text elements pop on the overlay */
    .hero-title-new {
        color: #ffffff !important;
    }
    .hero-subheding-new {
        color: #e2e8f0 !important;
    }
    
    /* Apply exact requested orange */
    .btn-primary-solid {
        background-color: #c85a1a !important;
        border-color: #c85a1a !important;
    }
}
""")

print("Hero full background mobile CSS applied!")
