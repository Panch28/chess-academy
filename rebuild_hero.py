import re

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

with open(f"{base_dir}\styles.css", "a", encoding="utf-8") as f:
    f.write("""
/* ==========================================================================
   STRICT HERO OVERRIDE PER LATEST RULES
   ========================================================================== */

/* Desktop Rules (> 768px) */
.hero.split-hero {
    display: flex !important;
    flex-direction: row !important;
    min-height: auto !important;
    height: auto !important;
    margin: 0 !important;
    padding: 0 !important;
    background-color: #1B2F5E !important;
    border-radius: 0 !important;
    box-shadow: none !important;
}

.hero-left {
    width: 50% !important;
    padding: 60px !important;
    background-color: #1B2F5E !important;
    flex: 1 1 50% !important;
    display: block !important;
}

.hero-right {
    width: 50% !important;
    flex: 1 1 50% !important;
    display: flex !important; /* critical for child to inherit stretch height */
    position: relative !important;
    overflow: hidden !important;
    height: auto !important;
    min-height: unset !important;
    margin: 0 !important;
    padding: 0 !important;
}

/* Image rules - strictly NO absolute, NO 100vh */
.hero-image-full {
    position: static !important;
    width: 100% !important;
    height: 100% !important;
    max-height: 100% !important;
    object-fit: cover !important;
    object-position: center top !important;
    display: block !important;
}

/* Mobile Rules (<= 768px) */
@media (max-width: 768px) {
    .hero.split-hero {
        flex-direction: column !important; /* Stack vertical, left text first */
    }
    
    .hero-left {
        width: 100% !important;
        flex: none !important;
    }
    
    .hero-right {
        width: 100% !important;
        height: 250px !important;
        flex: none !important;
        display: block !important; /* Reset display to let explicit height work */
    }
    
    .hero-image-full {
        height: 250px !important; /* Strict 250px constraint */
        width: 100% !important;
    }
    
    /* Restore the stats widgets that were potentially hidden earlier */
    .hero-trust-new {
        display: flex !important;
    }
}
""")

print("Hero Rebuild CSS Appended!")
