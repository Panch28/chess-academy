import re

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

# 1. Purge the old light theme override
with open(f"{base_dir}/styles.css", "r", encoding="utf-8") as f:
    css = f.read()

css = re.sub(r'/\* ==========================================================================\s*LIGHT THEME OVERRIDES.*', '', css, flags=re.DOTALL)

slate_css = """
/* ==========================================================================
   SLATE & STONE OVERRIDES
   ========================================================================== */

:root {
  --ss-bg: #F4F5F6;
  --ss-surface: #D8DCE0;
  --ss-grey: #A8B0B8;
  --ss-dark: #343C44;
  --ss-navy: #1B4B7A;
  --ss-white: #FFFFFF;
}

/* LAYOUT FIX - Edge to Edge Backgrounds */
body { background-color: var(--ss-bg) !important; }
.section, .bg-dark, .about-war-room, .achievements-banner, .footer {
    max-width: 100% !important;
    width: 100% !important;
    margin: 0 !important;
    border-radius: 0 !important;
}
.container {
    max-width: 1200px !important;
    margin: 0 auto !important;
    width: 90% !important;
}

/* Typography Overrides Core (Excluding Hero) */
.section:not(.hero) .section-subtitle {
    color: var(--ss-navy) !important;
    font-size: 12px !important;
    letter-spacing: 0.1em !important;
    text-decoration: underline;
    text-decoration-color: var(--ss-navy);
    text-decoration-thickness: 2px;
}
.section:not(.hero) .section-title, .section:not(.hero) h2 {
    color: var(--ss-dark) !important;
    font-weight: 700 !important;
}
.section:not(.hero) p, .section:not(.hero) .text-light, .section:not(.hero) .body-text {
    color: var(--ss-grey) !important;
}

/* NAVIGATION BAR */
.navbar { background: var(--ss-dark) !important; }
.navbar .nav-link { color: var(--ss-bg) !important; }
.navbar .logo, .navbar .logo span { color: var(--ss-white) !important; }
.navbar .btn { background: var(--ss-navy) !important; color: var(--ss-white) !important; border-radius: 24px !important; border:none!important;}

/* WHY CHESS & WHY CHOOSE US */
#why-chess { background: var(--ss-bg) !important; }
.benefit-card, .feature-item {
    background: var(--ss-white) !important;
    border: 1px solid var(--ss-surface) !important;
    border-radius: 12px !important;
    box-shadow: none !important;
}
.benefit-icon i, .feature-icon i, .gold-icon { color: var(--ss-navy) !important; }
.benefit-card h3 { color: var(--ss-navy) !important; font-weight: 600 !important; }
.feature-item h4 { color: var(--ss-dark) !important; font-weight: 600 !important; }
.why-choose-us .subsection-title { color: var(--ss-dark) !important; }

/* ABOUT OUR ACADEMY */
#about { background: var(--ss-white) !important; }
.accordion-item, .info-box { border-left: 3px solid var(--ss-navy) !important; }
.about-content h3, .accordion-header h3 { color: var(--ss-dark) !important; }
.accordion-icon { color: var(--ss-navy) !important; }
.stat-item h3 { color: var(--ss-navy) !important; }
.stat-item p { color: var(--ss-dark) !important; }

/* ACHIEVEMENTS BANNER */
.achievements-banner { background: var(--ss-dark) !important; }
.achievements-banner h2 { color: var(--ss-bg) !important; }
.achievements-banner i, .achievements-banner .trophy-icon { color: var(--ss-white) !important; }

/* GALLERY / VISUALS */
#gallery { background: var(--ss-white) !important; }
.gallery-nav-btn { background: var(--ss-dark) !important; color: var(--ss-white) !important; border: none !important; }
.gallery-nav-btn i { color: var(--ss-white) !important; }
.gallery-item-3d, .gallery-item-3d img { border: 1px solid var(--ss-surface) !important; }

/* OUR TEACHERS & EXPERTS */
#teachers { background: var(--ss-bg) !important; }
.teacher-featured, .teacher-card { background: var(--ss-white) !important; border: 1px solid var(--ss-surface) !important; box-shadow: none !important; }
.teacher-badge { background: var(--ss-surface) !important; color: var(--ss-navy) !important; }
.teacher-info h3, .teacher-info h4 { color: var(--ss-dark) !important; }
.teacher-role { color: var(--ss-grey) !important; }

/* TESTIMONIALS */
#testimonials { background: var(--ss-white) !important; }
.testimonial-card, .testimonial-item { background: var(--ss-bg) !important; border: 1px solid var(--ss-surface) !important; box-shadow:none!important;}
.testimonial-badge { background: var(--ss-surface) !important; color: var(--ss-dark) !important; }
.stars i, .testimonial-stars i { color: var(--ss-navy) !important; }
.testimonial-text { color: var(--ss-dark) !important; font-style: italic !important; }
.reviewer-name { color: var(--ss-dark) !important; font-weight: 600 !important; }
.reviewer-relation, .reviewer-role { color: var(--ss-grey) !important; }
.carousel-dot.active { background: var(--ss-navy) !important; }
.carousel-dot { background: var(--ss-surface) !important; }

/* COURSES & ACTIVITIES */
#courses { background: var(--ss-bg) !important; }
.course-card { background: var(--ss-white) !important; border: 1px solid var(--ss-surface) !important; border-radius: 12px !important; box-shadow:none!important;}
.badge.bg-gold { background: var(--ss-navy) !important; color: var(--ss-white) !important; }
.course-icon i { color: var(--ss-dark) !important; }
.course-card h3 { color: var(--ss-dark) !important; }
.course-features li i { color: var(--ss-navy) !important; }
.course-card .btn { background: transparent !important; border: 1px solid var(--ss-navy) !important; color: var(--ss-navy) !important; }
.course-card.popular .btn { background: var(--ss-navy) !important; color: var(--ss-white) !important; }

/* UPCOMING EVENTS & COUNTDOWN */
#events { background: var(--ss-white) !important; } /* Alternating clean bg */
.event-card, .countdown-card { background: var(--ss-dark) !important; border-radius: 12px; }
.countdown-box span.label, .countdown-label { color: var(--ss-grey) !important; }
.countdown-box span.number, .countdown-number { color: var(--ss-bg) !important; }
.event-card .btn { background: var(--ss-navy) !important; color: var(--ss-white) !important; border:none!important;}

/* BATCH SCHEDULE */
#schedule { background: var(--ss-bg) !important; }
.schedule-card { background: var(--ss-white) !important; border: 1px solid var(--ss-surface) !important; box-shadow:none!important;}
.schedule-badge.popular { background: var(--ss-surface) !important; color: var(--ss-dark) !important; }
.schedule-badge.best { background: var(--ss-navy) !important; color: var(--ss-white) !important; }
.schedule-badge.available { background: var(--ss-surface) !important; color: var(--ss-grey) !important; }
.schedule-time { background: var(--ss-bg) !important; border: 1px solid var(--ss-surface) !important; color: var(--ss-dark) !important; }
.schedule-details li i { color: var(--ss-navy) !important; }
.schedule-card .btn { background: transparent !important; border: 1px solid var(--ss-navy) !important; color: var(--ss-navy) !important; }
.schedule-card.featured .btn { background: var(--ss-navy) !important; color: var(--ss-white) !important; }

/* CONTACT & REGISTRATION */
#contact { background: var(--ss-white) !important; }
.contact-info { background: var(--ss-dark) !important; }
.info-item p { color: var(--ss-bg) !important; }
.info-item h4 { color: var(--ss-grey) !important; }
.info-icon { background: var(--ss-navy) !important; color: var(--ss-white) !important; }
.contact-form .btn-primary { background: var(--ss-navy) !important; color: var(--ss-white) !important; border:none!important;}
.contact-form .btn-outline { background: transparent !important; border: 1px solid var(--ss-surface) !important; color: var(--ss-dark) !important; }
.map-embed { border: 1px solid var(--ss-surface) !important; }

/* FOOTER */
.footer { background: var(--ss-dark) !important; border-top: 1px solid rgba(255,255,255,0.1) !important; padding-top:60px!important; padding-bottom:30px!important;}
.footer-logo, .footer-logo span { color: var(--ss-white) !important; }
.footer p, .footer-bottom p { color: var(--ss-grey) !important; }
.footer h3, .footer-widget h4 { color: var(--ss-bg) !important; }
.footer-links li a { color: var(--ss-grey) !important; text-decoration: none!important; }
.footer-links li a:hover { color: var(--ss-bg) !important; text-decoration:underline!important;}
.whatsapp-float { background: var(--ss-navy) !important; color: var(--ss-white) !important; }
.whatsapp-float i { color: var(--ss-white) !important; }
"""

with open(f"{base_dir}/styles.css", "w", encoding="utf-8") as f:
    f.write(css + "\n" + slate_css)

print("Slate & Stone Overrides applied.")
