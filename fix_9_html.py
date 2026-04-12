import re
import os

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

with open(f"{base_dir}/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# -------------------------------------------------------------
# Fix 9: Add Contact/WhatsApp CTA instead of Registration Form
# -------------------------------------------------------------

new_form_html = """
                    <div class="contact-cta-section scroll-reveal delay-1">
                        <h3 class="text-white mb-4">Get in Touch</h3>
                        <p class="text-light mb-4">Interested in enrolling or have questions? Reach out to us directly through WhatsApp or give us a call!</p>
                        
                        <a href="https://wa.me/919876543210?text=Hi,%20I'm%20interested%20in%20enrolling%20at%20Sri%20Sai%20Chess%20Academy" 
                           target="_blank" class="btn btn-primary w-100 mb-3" style="background-color: #c85a1a; border-color: #c85a1a; border-radius: 8px;">
                            <i class="fa-brands fa-whatsapp"></i> WhatsApp Us
                        </a>
                        
                        <a href="tel:+919876543210" class="btn btn-outline-gold w-100 mb-3" style="border-radius: 8px; color: #ffffff; border-color: #ffffff;">
                            <i class="fa-solid fa-phone"></i> Call Now
                        </a>
                        
                        <a href="mailto:info@srisaichess.com" class="btn btn-outline-gold w-100" style="border-radius: 8px; color: #ffffff; border-color: #ffffff;">
                            <i class="fa-solid fa-envelope"></i> Email Us
                        </a>
                    </div>
"""

# Replace the form with our new CTA block
html = re.sub(r'<form class="contact-form.*?</form>', new_form_html, html, flags=re.DOTALL)


# -------------------------------------------------------------
# Fix 4: Restore Stats layout so JS runs correctly
# -------------------------------------------------------------
# Let's see if we had replaced it with static text previously
html = html.replace('<span class="stat-number-static">500+</span>', '<span class="stat-number" data-count="500">0</span>')
html = html.replace('<span class="stat-number-static">50+</span>', '<span class="stat-number" data-count="50">0</span>')
html = html.replace('<span class="stat-number-static">15+</span>', '<span class="stat-number" data-count="15">0</span>')
# In teachers section
html = html.replace('<span class="stat-value">15+</span>', '<span class="stat-number stat-value" data-count="15">0</span>')
html = html.replace('<span class="stat-value">500+</span>', '<span class="stat-number stat-value" data-count="500">0</span>')
html = html.replace('<span class="stat-value">50+</span>', '<span class="stat-number stat-value" data-count="50">0</span>')


with open(f"{base_dir}/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML script changes complete.")
