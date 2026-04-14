import os

css_overrides = """
/* ==========================================================================
   TEXT VISIBILITY OVERRIDES
   ========================================================================== */

/* General Body text */
body, .section { color: #1B2F5E; }
.bg-dark, .hero, .footer, .about-war-room, .achievements-banner, 
.feature-card, .benefit-card, .course-card, .schedule-card, 
.event-card, .teacher-card, .teacher-featured, .testimonial-card, 
.activity-card, .contact-info, .gallery-item-3d, .feature-item {
    color: #FFFFFF;
}

/* General Headings */
h1, h2, h3, h4, h5, h6 { color: #1B2F5E; }
.bg-dark h1, .bg-dark h2, .bg-dark h3, .bg-dark h4, .bg-dark h5, .bg-dark h6,
.hero h1, .hero h2, .hero h3, .hero h4, .hero h5, .hero h6,
.footer h1, .footer h2, .footer h3, .footer h4, .footer h5, .footer h6,
.about-war-room h1, .about-war-room h2, .about-war-room h3, .about-war-room h4, .about-war-room h5, .about-war-room h6,
.achievements-banner h1, .achievements-banner h2, .achievements-banner h3, .achievements-banner h4, .achievements-banner h5, .achievements-banner h6,
.contact-info h1, .contact-info h2, .contact-info h3, .contact-info h4, .contact-info h5, .contact-info h6,
.feature-card h3, .benefit-card h3, .course-card h3, .schedule-card h3, 
.event-card h3, .teacher-card h4, .teacher-featured h3, .activity-card h4, .feature-item h4 {
    color: #FFFFFF !important;
}

/* Specific Section Fixes */

/* Hero */
.hero p, .hero-tagline, .hero-testimonial p { color: #E0E6F0 !important; }
.hero-testimonial span { color: #E0E6F0 !important; }

/* Benefits Cards */
.benefit-card p, .feature-card p { color: #E0E6F0 !important; }

/* About Academy section */
.huge-stat .stat-number, .huge-stat .plus-sign { color: #E85D04 !important; }
.huge-stat-label { color: #FFFFFF !important; }
.strip-text p, .banner-text p { color: #E0E6F0 !important; }
.strip-text h3, .banner-text h4, .about-content-right .section-title { color: #FFFFFF !important; }

/* Why Choose Us cards */
.feature-item p { color: #E0E6F0 !important; }

/* Courses cards */
.course-card p, .course-details li, .course-meta span { color: #E0E6F0 !important; }

/* Batch Schedule cards */
.schedule-time span, .schedule-details li { color: #E0E6F0 !important; }

/* Events section */
.events-grid .event-card p, .event-meta span, .event-date span { color: #FFFFFF !important; }
.countdown-number, .countdown-label, .countdown-separator { color: #FFFFFF !important; }
.countdown-wrapper h3 { color: #FFFFFF !important; }
.event-tag, .schedule-badge { color: #1B2F5E !important; }

/* Activities */
.activity-card p { color: #E0E6F0 !important; }

/* Teachers */
.teacher-role, .role, .bio, .teacher-stats .stat-name { color: #E0E6F0 !important; }
.teacher-stats .stat-value { color: #FFFFFF !important; }

/* Testimonials */
.testimonial-card p { color: #FFFFFF !important; }
.testimonial-author h5 { color: #FFFFFF !important; }
.testimonial-author span { color: #B0BDD6 !important; }

/* Contact section */
.contact-info *, .contact-info h3, .contact-info h4, .contact-info p { color: #FFFFFF !important; }
.contact-form h3, .contact-form label, .contact-form input, .contact-form select, .contact-form textarea { color: #1B2F5E !important; }
/* Ensure form inputs have white background for readability */
.contact-form input, .contact-form select, .contact-form textarea {
    background-color: #FFFFFF !important;
}

/* Footer */
.footer p, .footer-links a, .footer-bottom p, .footer .text-light { color: #B0BDD6 !important; }
.footer-links a:hover { color: #FFFFFF !important; }
.footer-logo span { color: #FFFFFF !important; }

/* Icons */
/* Light Backgrounds */
.section:not(.bg-dark):not(.about-war-room):not(.achievements-banner) i:not(.hero i):not(.footer i):not(.navbar i):not(.stars i):not(.gold-icon) {
    color: #3A5FCD;
}

/* Icons on Dark Backgrounds */
.bg-dark i, .hero i, .about-war-room i, .footer i, 
.benefit-icon i, .feature-icon i, .course-icon i, 
.activity-icon i, .event-meta i, .schedule-time i, 
.schedule-details i, .info-icon i, .banner-icon i, .strip-icon i, .stars i, .gold-icon {
    color: #E85D04 !important;
}

/* Badges / Tags */
.badge, .testimonial-badge, .event-tag, .schedule-badge, .teacher-badge {
    color: #1B2F5E !important;
    background-color: #FFCC99 !important;
}
"""

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

with open(f"{base_dir}/styles.css", "a", encoding="utf-8") as f:
    f.write(css_overrides)

# Let's fix admin.html text as well, since it says "across the entire website"
admin_overrides = """
/* Admin Text Fixes */
body { color: #1B2F5E; }
.sidebar { background: #1B2F5E; color: #FFFFFF; }
.sidebar-menu li a { color: #E0E6F0; }
.sidebar-menu li.active a, .sidebar-menu li a:hover { color: #FFFFFF; }
.stat-card { color: #FFFFFF; } /* Assuming dark bg */
.stat-title { color: #B0BDD6; }
"""

with open(f"{base_dir}/admin.html", "r", encoding="utf-8") as f:
    content = f.read()

if "<style>" in content:
    content = content.replace("</style>", admin_overrides + "\n</style>")
    with open(f"{base_dir}/admin.html", "w", encoding="utf-8") as f:
        f.write(content)

print("CSS appended to styles.css and admin.html updated")
