import re
import os

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

with open(f"{base_dir}/styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Strip any previous overrides I added
css = re.sub(r'/\* ==========================================================================\s*(LIGHT THEME OVERRIDES|SLATE & STONE OVERRIDES|SLATE & STONE V2 OVERRIDES).*', '', css, flags=re.DOTALL)

# Build the new Forest & Gold CSS block
forest_css = """
/* ==========================================================================
   FOREST & GOLD V3 OVERRIDES (EXACT PALETTE & RULES)
   ========================================================================== */

:root {
  --v3-cream: #F5F2EB;
  --v3-white: #FFFFFF;
  --v3-linen: #E4DDD0;
  --v3-forest: #1A2E1A;
  --v3-emerald: #2D6A4F;
  --v3-navy: #0F2744;
  --v3-amber: #C8922A;
  --v3-body: #3D3D3D;
  --v3-sub: #555555;
  --v3-sage: #93BFA8;
}

/* ───────────────────────────────────────────────────────────────
   GLOBAL RULES
─────────────────────────────────────────────────────────────── */
body {
    background-color: var(--v3-cream) !important;
    max-width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow-x: hidden !important;
}

/* Full bleed sections */
.section, .about-war-room, .achievements-banner, .footer, .navbar {
    max-width: 100% !important;
    width: 100% !important;
    margin: 0 !important;
    border-radius: 0 !important;
}

/* Inner content centering */
.container {
    max-width: 1200px !important;
    margin: 0 auto !important;
    width: 90% !important;
}

/* Typography globals - EXCLUDE HERO */
.section:not(.hero) .section-subtitle {
    color: var(--v3-emerald) !important;
    font-size: 12px !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    text-decoration: underline !important;
    text-decoration-color: var(--v3-amber) !important;
    text-decoration-thickness: 2px !important;
    text-underline-offset: 4px !important;
}
.section:not(.hero) .section-title, .section:not(.hero) h2, .section:not(.hero) h1 {
    color: var(--v3-forest) !important;
    font-weight: 700 !important;
}
.section:not(.hero) p, .section:not(.hero) .text-light, .section:not(.hero) .body-text {
    color: var(--v3-body) !important;
}

/* Global button/card behaviors */
.card, .benefit-card, .feature-item, .course-card, .schedule-card, .teacher-card, .teacher-featured, .testimonial-card {
    background-color: var(--v3-white) !important;
    border: 1px solid var(--v3-linen) !important;
    border-radius: 12px !important;
    box-shadow: none !important;
}
.btn, button { border-radius: 24px !important; }

/* ───────────────────────────────────────────────────────────────
   SECTION BY SECTION
─────────────────────────────────────────────────────────────── */

/* NAVIGATION BAR */
#navbar { background: var(--v3-forest) !important; }
.nav-link { color: var(--v3-white) !important; }
.nav-link:hover, .nav-link.active { color: var(--v3-amber) !important; text-decoration: none !important;}
.navbar .logo, .navbar .logo span { color: var(--v3-white) !important; }
.navbar .btn { background: var(--v3-amber) !important; color: var(--v3-white) !important; border: none !important; }
/* Assuming there is an announcement bar, normally it's at top. Let's cover top-bar class if exists */
.top-bar { background: var(--v3-navy) !important; color: var(--v3-white) !important; }

/* BENEFITS OF LEARNING CHESS & WHY CHOOSE US (#why-chess / .why-choose-us) */
#why-chess, .why-choose-us { background: var(--v3-cream) !important; }
.benefit-card h3, .feature-item h3 { color: var(--v3-forest) !important; }
.why-choose-us .feature-item h4, .why-choose-us .feature-item h3 { color: var(--v3-forest) !important; font-weight: 600 !important; }
.benefit-icon i, .feature-icon i { color: var(--v3-emerald) !important; }
.why-choose-us .subsection-title i.fa-star { color: var(--v3-amber) !important; }
.why-choose-us .subsection-title { color: var(--v3-forest) !important; }
.benefit-card p, .feature-item p { color: var(--v3-body) !important; }

/* ABOUT OUR ACADEMY */
#about { background: var(--v3-white) !important; }
.accordion-item, .info-box { border-left: 3px solid var(--v3-amber) !important; border-radius:0 !important; }
.accordion-icon { color: var(--v3-emerald) !important; } /* PLUS/MINUS */
.about-content i { color: var(--v3-emerald) !important; } /* Eye, target, flag */
.about-content h2, .about-content h3, .accordion-header h3 { color: var(--v3-forest) !important; }
.about-content p, .accordion-body { color: var(--v3-body) !important; }
.stat-item h3 { color: var(--v3-amber) !important; } /* 500+, 50+ */
.stat-item p { color: var(--v3-sub) !important; }

/* OUR ACHIEVEMENTS BANNER */
.achievements-banner { background: var(--v3-navy) !important; }
.achievements-banner h2 { color: var(--v3-white) !important; }
.achievements-banner p { color: var(--v3-linen) !important; }
.achievements-banner i, .trophy-icon { color: var(--v3-amber) !important; }

/* GALLERY / VISUALS */
#gallery { background: var(--v3-white) !important; }
.gallery-nav-btn { background: var(--v3-forest) !important; color: var(--v3-white) !important; border: none !important; }
.gallery-nav-btn i { color: var(--v3-white) !important; }
.gallery-item-3d, .gallery-item-3d img { border: 1px solid var(--v3-linen) !important; }
.gallery-overlay-text { background: rgba(26,46,26,0.7) !important; color: var(--v3-white) !important; }

/* OUR TEACHERS & EXPERTS */
#teachers { background: var(--v3-cream) !important; }
.teacher-badge { background: var(--v3-amber) !important; color: var(--v3-white) !important; border-radius: 20px !important;}
.teacher-info h3 { color: var(--v3-forest) !important; font-weight: 700 !important; }
.teacher-info h4 { color: var(--v3-forest) !important; font-weight: 600 !important; } /* small cards */
.teacher-role, .teacher-info .role-label { color: var(--v3-sub) !important; text-transform: uppercase !important; } /* Job Title */
.teacher-info p { color: var(--v3-body) !important; }
.teacher-skill-tag { background: var(--v3-cream) !important; color: var(--v3-emerald) !important; border: 1px solid var(--v3-linen) !important; }

/* TESTIMONIALS / WHAT PARENTS SAY */
#testimonials { background: var(--v3-white) !important; }
.testimonial-card, .testimonial-item { background: var(--v3-cream) !important; border: 1px solid var(--v3-linen) !important; }
.stars i, .testimonial-stars i { color: var(--v3-amber) !important; }
.testimonial-text { color: var(--v3-body) !important; font-style: italic !important; }
.reviewer-name { color: var(--v3-forest) !important; font-weight: 600 !important; }
.reviewer-relation, .reviewer-role { color: var(--v3-sub) !important; }
.carousel-dot.active { background: var(--v3-emerald) !important; }
.carousel-dot { background: var(--v3-linen) !important; }
.testimonial-nav-btn { border: 1px solid var(--v3-linen) !important; color: var(--v3-forest) !important; background: transparent !important; }
.testimonial-badge, .success-badge { background: var(--v3-linen) !important; color: var(--v3-forest) !important; border-radius: 20px !important;}
.testimonial-avatar { border: 2px solid var(--v3-amber) !important; }

/* COURSES & ACTIVITIES */
#courses { background: var(--v3-cream) !important; }
.course-icon i { color: var(--v3-forest) !important; } /* Assuming pieces are 343C44 equivalent which is Forest Dark or Body? Rules say #343C44, wait previous rules said #1A2E1A in the V3: Card chess piece icons -> #1A2E1A */
.course-icon i { color: var(--v3-forest) !important; }
.course-card h3 { color: var(--v3-forest) !important; font-weight:700!important; }
.badge.bg-gold, .course-badge.popular { background: var(--v3-navy) !important; color: var(--v3-white) !important; border-radius: 20px !important;} /* MOST POPULAR badge */
.course-features li i { color: var(--v3-emerald) !important; } /* Checklist tick marks */
.course-info-box { background: var(--v3-cream) !important; color: var(--v3-sub) !important; border: 1px solid var(--v3-linen) !important; }
.course-age-icon { color: var(--v3-emerald) !important; }
.course-duration-icon { color: var(--v3-amber) !important; }
.course-features li { color: var(--v3-body) !important; }
/* Default Enroll */
.course-card .btn { background: transparent !important; border: 2px solid var(--v3-forest) !important; color: var(--v3-forest) !important; }
/* Featured Enroll */
.course-card.popular .btn { background: var(--v3-navy) !important; color: var(--v3-white) !important; border: none !important; }

/* EVENTS & TOURNAMENTS */
#events { background: var(--v3-white) !important; }
.event-card, .countdown-card { background: var(--v3-navy) !important; border: none !important; }
.countdown-box span.label, .countdown-label { color: var(--v3-sage) !important; }
.countdown-box span.number, .countdown-number { color: var(--v3-white) !important; font-size: 2rem!important; font-weight: bold!important; }
.countdown-card h3 { color: var(--v3-linen) !important; text-transform: uppercase !important; letter-spacing: 0.1em !important; }
.event-card .btn, .countdown-btn { background: var(--v3-amber) !important; color: var(--v3-white) !important; border:none!important; }

/* Event Date Cards (Tournament / Camp) */
.event-date-card { background: var(--v3-forest) !important; }
.event-date-box { background: var(--v3-amber) !important; color: var(--v3-white) !important; }
.event-date-box span { color: var(--v3-white) !important; font-weight:bold!important; font-size:1.5rem!important; }
.event-tag { background: var(--v3-amber) !important; color: var(--v3-white) !important; border-radius: 20px!important; }
.event-info h3 { color: var(--v3-white) !important; font-weight: 600!important;}
.event-info p { color: var(--v3-linen) !important; }
.event-meta .time-icon { color: var(--v3-amber) !important; }
.event-meta .loc-icon { color: var(--v3-sage) !important; }
.event-meta i { color: var(--v3-amber) !important; } /* Fallback */

/* BATCH SCHEDULE */
#schedule { background: var(--v3-cream) !important; }
.schedule-card { background: var(--v3-white) !important; border: 1px solid var(--v3-linen) !important; box-shadow:none!important;}
.schedule-badge.popular { background: var(--v3-linen) !important; color: var(--v3-forest) !important; }
.schedule-badge.best { background: var(--v3-amber) !important; color: var(--v3-white) !important; }
.schedule-badge.available { background: var(--v3-linen) !important; color: var(--v3-sub) !important; }
.schedule-time { background: var(--v3-cream) !important; border: 1px solid var(--v3-linen) !important; color: var(--v3-forest) !important; font-weight: 500!important;}
.schedule-time i { color: var(--v3-emerald) !important; }
.schedule-details li i { color: var(--v3-emerald) !important; }
.schedule-details li { color: var(--v3-body) !important; }
/* Enroll default vs featured */
.schedule-card .btn { background: transparent !important; border: 2px solid var(--v3-forest) !important; color: var(--v3-forest) !important; }
.schedule-card.featured .btn, .schedule-card.best .btn { background: var(--v3-navy) !important; color: var(--v3-white) !important; border:none!important;}

/* CONTACT & REGISTRATION */
#contact { background: var(--v3-white) !important; }
.contact-info { background: var(--v3-navy) !important; }
.contact-info h2, .contact-info h3, .contact-info h4 { color: var(--v3-white) !important; }
.info-item h4 { color: var(--v3-sage) !important; } /* Info card heading/labels -> sage */
.info-item p { color: var(--v3-white) !important; } /* Info card values -> white (wait rule says white) */
.info-icon { background: var(--v3-amber) !important; color: var(--v3-white) !important; }
.contact-form .btn-primary { background: var(--v3-amber) !important; color: var(--v3-white) !important; border:none!important; width:100%!important;} /* WHATSAPP US */
/* Call Now / Email Us */
.contact-form .btn-outline { background: transparent !important; border: 2px solid var(--v3-navy) !important; color: var(--v3-navy) !important; } /* Wait rule says border "#0F2744" */
/* Map Embed */
.map-embed { border: 1px solid var(--v3-linen) !important; }

/* FOOTER */
.footer { background: var(--v3-forest) !important; border-top: 1px solid rgba(255,255,255,0.1) !important; padding-top:60px!important; padding-bottom:30px!important;}
.footer-logo, .footer-logo span { color: var(--v3-white) !important; }
.footer p, .footer-bottom p, .footer-tagline { color: var(--v3-sage) !important; }
.footer h3, .footer-widget h4 { color: var(--v3-white) !important; font-weight: 600 !important; text-transform: uppercase !important; }
.footer-links li a { color: var(--v3-sage) !important; text-decoration: none!important; }
.footer-links li a:hover { color: var(--v3-white) !important; text-decoration:underline!important;}
.footer-copyright { color: var(--v3-sage) !important; }
.whatsapp-float { background: var(--v3-amber) !important; color: var(--v3-white) !important; }
.whatsapp-float i { color: var(--v3-white) !important; }

/* ENSURE DARK BACKGROUNDS OVERRIDE EVERYTHING FOR TEXT */
.bg-dark h1, .bg-dark h2, .bg-dark h3, .bg-dark p, .bg-dark span,
.contact-info h1, .contact-info h2, .contact-info h3, .contact-info p, .contact-info span,
.achievements-banner h1, .achievements-banner h2, .achievements-banner h3, .achievements-banner p, .achievements-banner span {
    /* Base rule will fallback safely */
}

/* Hard explicit exceptions based on rules */
.achievements-banner h2 { color: var(--v3-white) !important; }
.achievements-banner p { color: var(--v3-linen) !important; }
.contact-info h2 { color: var(--v3-white) !important; }

"""

with open(f"{base_dir}/styles.css", "w", encoding="utf-8") as f:
    f.write(css.strip() + "\n\n" + forest_css)

print("Master Forest & Gold V3 applied.")
