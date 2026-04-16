import re
import os

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

# 1. Update text "Expert Level" to "Advanced Level" in HTML
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace(">Expert Level<", ">Advanced Level<")
with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)


# 2. Append Custom Light Theme Overrides safely to styles.css
overrides = """
/* ==========================================================================
   LIGHT THEME OVERRIDES (CLIENT REQUEST)
   ========================================================================== */

/* Change dark section backgrounds to light cement/grey */
.bg-dark {
    background-color: #f5f5f5 !important;
    backdrop-filter: none !important;
    -webkit-backdrop-filter: none !important;
}

.about-war-room {
    background-color: #f5f5f5 !important;
}

/* Change target cards from navy/dark to pure white */
.feature-card, .benefit-card, .course-card, .schedule-card, 
.event-card, .teacher-card, .teacher-featured, .testimonial-card, 
.activity-card, .feature-item {
    background-color: #ffffff !important;
    background: #ffffff !important; /* clear gradients if any */
    border: 1px solid rgba(27, 47, 94, 0.1) !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05) !important;
}

/* Force text in these components to be dark blue or black */
.bg-dark, .about-war-room,
.feature-card, .benefit-card, .course-card, .schedule-card, 
.event-card, .teacher-card, .teacher-featured, .testimonial-card, 
.activity-card, .feature-item {
    color: #1A1A1A !important;
}

.bg-dark p, .about-war-room p,
.feature-card p, .benefit-card p, .course-card p, .schedule-card p, 
.event-card p, .teacher-card p, .teacher-featured p, .testimonial-card p, 
.activity-card p, .feature-item p {
    color: #333333 !important;
}

/* Force headings in these components to be Brand Dark Blue (#1B2F5E) */
.bg-dark h1, .bg-dark h2, .bg-dark h3, .bg-dark h4, .bg-dark h5, .bg-dark h6,
.about-war-room h1, .about-war-room h2, .about-war-room h3, .about-war-room h4, .about-war-room h5, .about-war-room h6,
.feature-card h3, .benefit-card h3, .course-card h3, .schedule-card h3, 
.event-card h3, .teacher-card h4, .teacher-featured h3, .activity-card h4, .feature-item h4 {
    color: #1B2F5E !important;
}

/* Remove all Orange icons globally inside these active boxes and sections, and make them Brand Dark Blue */
.bg-dark i, .about-war-room i, 
.benefit-icon i, .feature-icon i, .course-icon i, 
.activity-icon i, .event-meta i, .schedule-time i, 
.schedule-details i, .info-icon i, .feature-item i, .gold-icon, .stars i {
    color: #1B2F5E !important;
}

/* Subheadings that used to be orange ('gold-text') should now be dark blue too */
.gold-text {
    color: #1B2F5E !important;
}
"""

with open(os.path.join(base_dir, "styles.css"), "a", encoding="utf-8") as f:
    f.write(overrides)

print("Light Theme applied successfully.")
