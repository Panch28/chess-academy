import re

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

with open(f"{base_dir}\styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# We will just append the most deterministic !important rules to ensure the card style matches perfectly.
# Any conflicting old rules will be suppressed by the density of these !important tags.

final_override = """
/* ==========================================================================
   ULTIMATE MOBILE HERO FIX (MATCHING CHESSKLUB REFERENCE)
   ========================================================================== */
@media (max-width: 992px) {
    /* Create the card effect on mobile */
    .hero.split-hero {
        display: flex !important;
        flex-direction: column !important; /* Ensure left (text) is above right (img) */
        margin: 20px !important; /* Create white space around the dark card */
        padding: 0 !important;
        background-color: #1a1a1a !important; /* Darker background resembling reference */
        border-radius: 20px !important;
        overflow: hidden !important; /* Clip the image cleanly at the bottom! */
        min-height: auto !important;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1) !important;
    }
    
    /* Body background behind card must be light */
    body {
        background-color: #FFFFFF !important;
    }

    .hero-left {
        width: 100% !important;
        padding: 40px 25px 20px 25px !important; /* Top padding, side padding, let bottom breathe into image */
        background-color: transparent !important;
        flex: 1 1 auto !important;
    }

    /* Fix the button stacks */
    .hero-buttons-new {
        display: flex !important;
        flex-direction: column !important;
        gap: 15px !important;
        margin-bottom: 30px !important;
    }
    .hero-buttons-new .btn {
        width: 100% !important;
        text-align: center !important;
        border-radius: 8px !important; /* Less pill, more rectangle like reference */
    }

    /* Force the image container to appear */
    .hero-right {
        display: block !important;
        width: 100% !important;
        height: 350px !important; /* Explicit height */
        min-height: unset !important;
        position: relative !important;
        margin: 0 !important;
        padding: 0 !important;
        flex: 0 0 auto !important; /* Don't shrink or grow */
        overflow: hidden !important;
    }

    /* Force the image to cover exactly */
    .hero-image-full {
        display: block !important;
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 100% !important;
        object-fit: cover !important;
        object-position: center top !important; /* Focus on face/board */
        opacity: 1 !important;
        visibility: visible !important;
        z-index: 5 !important;
    }

    /* Hide the stats block on mobile to match the exact clean reference if desired, 
       or just let it sit cleanly above the image. The user reference has NO stats. */
    .hero-trust-new {
        display: none !important;
    }

    /* Optional: Subheading subtle grey */
    .hero-subheding-new {
        color: #d1d5db !important; 
        font-size: 16px !important;
        line-height: 1.6 !important;
        margin-bottom: 30px !important;
    }
    .hero-title-new {
        font-size: 32px !important;
        margin-top: 15px !important;
    }
}
"""

with open(f"{base_dir}\styles.css", "a", encoding="utf-8") as f:
    f.write(final_override)

print("Applied final reference overrides!")
