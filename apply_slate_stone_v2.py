import re
import os

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

with open(f"{base_dir}/styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Strip any previous overrides I added
css = re.sub(r'/\* ==========================================================================\s*(LIGHT THEME OVERRIDES|SLATE & STONE OVERRIDES).*', '', css, flags=re.DOTALL)

# Now, we craft the new masterful CSS based strictly on the user's explicit prompt.
slate_css = """
/* ==========================================================================
   SLATE & STONE V2 OVERRIDES (EXACT PALETTE & RULES)
   ========================================================================== */

:root {
  --ss-bg: #F4F5F6;
  --ss-white: #FFFFFF;
  --ss-stone: #D8DCE0;
  --ss-navy: #1B4B7A;
  --ss-charcoal: #343C44;
  --ss-amber: #D4943A;
}

/* ───────────────────────────────────────────────────────────────
   GLOBAL RULES
─────────────────────────────────────────────────────────────── */
body {
    background-color: var(--ss-bg) !important;
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
    color: var(--ss-navy) !important;
    text-decoration: underline !important;
    text-decoration-color: var(--ss-amber) !important;
    text-decoration-thickness: 2px !important;
    text-underline-offset: 4px !important;
}
.section:not(.hero) .section-title, .section:not(.hero) h2, .section:not(.hero) h1 {
    color: var(--ss-charcoal) !important;
    font-weight: 700 !important;
}
.section:not(.hero) p, .section:not(.hero) .text-light, .section:not(.hero) .body-text {
    color: var(--ss-grey, #A8B0B8) !important;
}

/* Global button/card behaviors */
.card, .benefit-card, .feature-item, .course-card, .schedule-card, .teacher-card, .teacher-featured, .testimonial-card {
    background-color: var(--ss-white) !important;
    border: 1px solid var(--ss-stone) !important;
    border-radius: 12px !important;
    box-shadow: none !important;
}
.btn, button { border-radius: 24px !important; }

/* ───────────────────────────────────────────────────────────────
   SECTION BY SECTION
─────────────────────────────────────────────────────────────── */

/* NAVIGATION BAR */
#navbar { background: var(--ss-charcoal) !important; }
.nav-link { color: var(--ss-bg) !important; }
.nav-link:hover, .nav-link.active { color: var(--ss-white) !important; }
.navbar .logo, .navbar .logo span { color: var(--ss-white) !important; }
.navbar .btn { background: var(--ss-amber) !important; color: var(--ss-white) !important; border: none !important; }

/* BENEFITS OF LEARNING CHESS & WHY CHOOSE US (#why-chess / .why-choose-us) */
#why-chess, .why-choose-us { background: var(--ss-bg) !important; }
.benefit-card h3, .feature-item h3 { color: var(--ss-navy) !important; font-weight: 600 !important; }
/* Wait, why choose us says: Card titles -> #343C44 */
.why-choose-us .feature-item h4, .why-choose-us .feature-item h3 { color: var(--ss-charcoal) !important; font-weight: 600 !important; }
.benefit-icon i, .feature-icon i { color: var(--ss-navy) !important; }
.why-choose-us .subsection-title i.fa-star { color: var(--ss-amber) !important; }
.why-choose-us .subsection-title { color: var(--ss-charcoal) !important; }

/* ABOUT OUR ACADEMY */
#about { background: var(--ss-white) !important; }
.accordion-item, .info-box { border-left: 3px solid var(--ss-amber) !important; border-radius:0 !important; }
.accordion-icon { color: var(--ss-amber) !important; }
.about-content i { color: var(--ss-navy) !important; }
.about-content h2, .about-content h3, .accordion-header h3 { color: var(--ss-charcoal) !important; }
.stat-item h3 { color: var(--ss-navy) !important; }
.stat-item p { color: var(--ss-charcoal) !important; }

/* OUR ACHIEVEMENTS BANNER */
.achievements-banner { background: var(--ss-charcoal) !important; }
.achievements-banner h2 { color: var(--ss-white) !important; }
.achievements-banner p { color: var(--ss-grey, #A8B0B8) !important; }
.achievements-banner i, .trophy-icon { color: var(--ss-amber) !important; }

/* GALLERY / VISUALS */
#gallery { background: var(--ss-white) !important; }
.gallery-nav-btn { background: var(--ss-charcoal) !important; color: var(--ss-white) !important; border: none !important; }
.gallery-nav-btn i { color: var(--ss-white) !important; }
.gallery-item-3d, .gallery-item-3d img { border: 1px solid var(--ss-stone) !important; }

/* OUR TEACHERS & EXPERTS */
#teachers { background: var(--ss-bg) !important; }
.teacher-badge { background: var(--ss-amber) !important; color: var(--ss-white) !important; }
.teacher-info h3, .teacher-info h4 { color: var(--ss-charcoal) !important; }
.teacher-role { color: var(--ss-grey, #A8B0B8) !important; text-transform: uppercase !important; }
.teacher-info p { color: var(--ss-charcoal) !important; }

/* TESTIMONIALS / WHAT PARENTS SAY */
#testimonials { background: var(--ss-white) !important; }
.testimonial-card, .testimonial-item { background: var(--ss-bg) !important; border: 1px solid var(--ss-stone) !important; }
.stars i, .testimonial-stars i { color: var(--ss-amber) !important; }
.testimonial-text { color: var(--ss-charcoal) !important; font-style: italic !important; }
.reviewer-name { color: var(--ss-charcoal) !important; font-weight: 600 !important; }
.reviewer-relation, .reviewer-role { color: var(--ss-grey, #A8B0B8) !important; }
.carousel-dot.active { background: var(--ss-navy) !important; }
.carousel-dot { background: var(--ss-stone) !important; }
/* Arrow buttons -> border D8DCE0, icon 343C44 */
.testimonial-nav-btn { border: 1px solid var(--ss-stone) !important; color: var(--ss-charcoal) !important; background: transparent !important; }
.testimonial-badge, .success-badge { background: var(--ss-stone) !important; color: var(--ss-charcoal) !important; }

/* COURSES & ACTIVITIES */
#courses { background: var(--ss-bg) !important; }
.course-icon i { color: var(--ss-charcoal) !important; }
.course-card h3 { color: var(--ss-charcoal) !important; font-weight:700!important; }
.badge.bg-gold { background: var(--ss-navy) !important; color: var(--ss-white) !important; } /* MOST POPULAR badge */
.course-features li i { color: var(--ss-amber) !important; } /* Checklist tick marks */
/* Default Enroll */
.course-card .btn { background: transparent !important; border: 1px solid var(--ss-navy) !important; color: var(--ss-navy) !important; }
/* Featured Enroll */
.course-card.popular .btn { background: var(--ss-navy) !important; color: var(--ss-white) !important; border: none !important; }

/* EVENTS & TOURNAMENTS */
#events { background: var(--ss-white) !important; }
.event-card, .countdown-card { background: var(--ss-charcoal) !important; border: none !important; }
.countdown-box span.label, .countdown-label { color: var(--ss-grey, #A8B0B8) !important; }
.countdown-box span.number, .countdown-number { color: var(--ss-white) !important; font-size: 2rem!important;}
.event-card .btn, .countdown-btn { background: var(--ss-amber) !important; color: var(--ss-white) !important; border:none!important; }

/* Event Date Cards (Tournament / Camp) */
.event-date-box { background: var(--ss-amber) !important; color: var(--ss-white) !important; }
.event-date-box span { color: var(--ss-white) !important; }
.event-tag { background: var(--ss-amber) !important; color: var(--ss-white) !important; }
.event-info h3 { color: var(--ss-white) !important; }
.event-info p { color: var(--ss-grey, #A8B0B8) !important; }
.event-meta i { color: var(--ss-amber) !important; }

/* BATCH SCHEDULE */
#schedule { background: var(--ss-bg) !important; }
.schedule-badge.popular { background: var(--ss-stone) !important; color: var(--ss-charcoal) !important; }
.schedule-badge.best { background: var(--ss-amber) !important; color: var(--ss-white) !important; }
.schedule-badge.available { background: var(--ss-stone) !important; color: var(--ss-grey, #A8B0B8) !important; }
.schedule-time { background: var(--ss-bg) !important; border: 1px solid var(--ss-stone) !important; color: var(--ss-charcoal) !important; }
.schedule-details li i { color: var(--ss-navy) !important; }
/* Enroll default vs featured */
.schedule-card .btn { background: transparent !important; border: 1px solid var(--ss-navy) !important; color: var(--ss-navy) !important; }
.schedule-card.featured .btn, .schedule-card.best .btn { background: var(--ss-navy) !important; color: var(--ss-white) !important; border:none!important;}

/* CONTACT & REGISTRATION */
#contact { background: var(--ss-white) !important; }
.contact-info { background: var(--ss-navy) !important; }
.contact-info h2, .contact-info h3 { color: var(--ss-white) !important; }
.info-item h4 { color: var(--ss-white) !important; } /* Info card headings -> white */
.info-item p { color: var(--ss-bg) !important; } /* Info card values -> F4F5F6 */
.info-icon { background: var(--ss-amber) !important; color: var(--ss-white) !important; }
.contact-form .btn-primary { background: var(--ss-amber) !important; color: var(--ss-white) !important; border:none!important;} /* WHATSAPP US */
/* Call Now / Email Us */
.contact-form .btn-outline { background: transparent !important; border: 1px solid var(--ss-white) !important; color: var(--ss-white) !important; }
/* Assuming map iframe is wrapped in map-embed class */
.map-embed { border: 1px solid var(--ss-stone) !important; }

/* FOOTER */
.footer { background: var(--ss-charcoal) !important; border-top: 1px solid rgba(255,255,255,0.1) !important; padding-top:60px!important; padding-bottom:30px!important;}
.footer-logo, .footer-logo span { color: var(--ss-white) !important; }
.footer p, .footer-bottom p, .footer-tagline { color: var(--ss-grey, #A8B0B8) !important; }
.footer h3, .footer-widget h4 { color: var(--ss-white) !important; font-weight: 600 !important; }
.footer-links li a { color: var(--ss-grey, #A8B0B8) !important; text-decoration: none!important; }
.footer-links li a:hover { color: var(--ss-white) !important; text-decoration:underline!important;}
.whatsapp-float { background: var(--ss-amber) !important; color: var(--ss-white) !important; }
.whatsapp-float i { color: var(--ss-white) !important; }

"""

with open(f"{base_dir}/styles.css", "w", encoding="utf-8") as f:
    f.write(css.strip() + "\n\n" + slate_css)

print("Master Slate & Stone V2 applied.")
