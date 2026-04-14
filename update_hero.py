import re
import os

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

# 1. UPDATE HTML
with open(f"{base_dir}/index.html", "r", encoding="utf-8") as f:
    html = f.read()

new_hero_html = """        <section id="home" class="hero split-hero">
            <div class="hero-left">
                <div class="hero-content-inner">
                    <div class="hero-badge-new">
                        <i class="fa-solid fa-star"></i> Now Enrolling for Summer Batch 2026
                    </div>
                    
                    <h1 class="hero-title-new">
                        Building Smart Minds<br>
                        Through Chess
                        <span class="hero-title-underline"></span>
                    </h1>
                    
                    <p class="hero-subheding-new">Welcome to Sri Sai Chess Academy, where strategic brilliance meets passion. Elevate your game today with our expert coaching.</p>
                    
                    <div class="hero-buttons-new">
                        <a href="#courses" class="btn btn-primary-solid">Explore Courses</a>
                        <a href="#contact" class="btn btn-secondary-outline">Register Now</a>
                    </div>
                    
                    <div class="hero-trust-new">
                        <div class="trust-item">
                            <i class="fa-solid fa-users"></i>
                            <span>500+ Students</span>
                        </div>
                        <div class="trust-item">
                            <i class="fa-solid fa-trophy"></i>
                            <span>50+ Champions</span>
                        </div>
                        <div class="trust-item">
                            <i class="fa-solid fa-star"></i>
                            <span>4.9 Rating</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="hero-right">
                <img src="https://images.unsplash.com/photo-1529699211952-734e80c4d42b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Student playing chess" class="hero-image-full">
            </div>
        </section>"""

# Using regex to replace the old hero section
html = re.sub(r'<section id="home" class="hero">.*?</section>', new_hero_html, html, flags=re.DOTALL)

with open(f"{base_dir}/index.html", "w", encoding="utf-8") as f:
    f.write(html)

# 2. APPEND CSS 
new_css = """
/* ==========================================================================
   NEW HERO SPLIT LAYOUT & NAVBAR UPDATES
   ========================================================================== */

/* Navbar Overrides */
.navbar, .navbar.scrolled {
    background: #FFFFFF !important;
    border-bottom: 1px solid #E0E6F0;
}
.navbar .logo span, .navbar .logo i {
    color: #1B2F5E !important;
}
.nav-links a {
    color: #1B2F5E !important;
}
.nav-links a:hover, .nav-links a.active {
    color: #E85D04 !important;
}
.navbar .btn-primary, .navbar a[href="#contact"].btn {
    background: #E85D04 !important;
    color: #FFFFFF !important;
    border-radius: 30px !important; /* Rounded corners */
    border: none !important;
}
.mobile-menu-toggle .hamburger i {
    color: #1B2F5E !important;
}

/* Split Hero Layout */
.hero { /* disable old styles if they interfere */
    padding: 0 !important;
    display: block !important;
}

.split-hero {
    display: flex !important;
    min-height: 100vh;
    width: 100%;
    align-items: stretch;
    background: #1B2F5E;
}

.hero-left {
    width: 55%;
    background: #1B2F5E;
    display: flex;
    align-items: center;
    padding: 120px 5% 60px 10%; /* Account for navbar */
    position: relative;
    z-index: 2;
}

.hero-content-inner {
    max-width: 650px;
    width: 100%;
}

.hero-right {
    width: 45%;
    position: relative;
    overflow: hidden;
}

.hero-image-full {
    width: 100%;
    height: 100%;
    object-fit: cover;
    position: absolute;
    top: 0;
    left: 0;
}

/* Left Content Styles */
.hero-badge-new {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #E85D04;
    color: #FFFFFF;
    padding: 8px 20px;
    border-radius: 50px;
    font-size: 0.85rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 30px;
}
.hero-badge-new i { color: #FFFFFF !important; }

.hero-title-new {
    font-family: 'Cinzel', serif;
    font-size: 3.5rem;
    font-weight: 700;
    line-height: 1.2;
    color: #FFFFFF !important;
    margin-bottom: 25px;
    position: relative;
}

.hero-title-underline {
    display: block;
    width: 120px;
    height: 6px;
    background: #E85D04;
    border-radius: 3px;
    margin-top: 20px;
}

.hero-subheding-new {
    font-size: 1.1rem;
    line-height: 1.7;
    color: #E0E6F0 !important;
    margin-bottom: 40px;
    max-width: 90%;
}

.hero-buttons-new {
    display: flex;
    gap: 20px;
    margin-bottom: 50px;
}

.btn-primary-solid {
    background: #E85D04 !important;
    color: #FFFFFF !important;
    padding: 15px 35px;
    border-radius: 30px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s ease;
    border: 2px solid #E85D04;
}
.btn-primary-solid:hover {
    background: #C14A03 !important;
    border-color: #C14A03;
    transform: translateY(-2px);
}

.btn-secondary-outline {
    background: transparent !important;
    color: #FFFFFF !important;
    border: 2px solid #FFFFFF !important;
    padding: 15px 35px;
    border-radius: 30px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s ease;
}
.btn-secondary-outline:hover {
    background: rgba(255, 255, 255, 0.1) !important;
    transform: translateY(-2px);
}

/* Trust Stats */
.hero-trust-new {
    display: flex;
    gap: 40px;
    flex-wrap: wrap;
}

.trust-item {
    display: flex;
    align-items: center;
    gap: 12px;
}

.trust-item i {
    color: #E85D04 !important;
    font-size: 1.5rem;
}

.trust-item span {
    color: #FFFFFF !important;
    font-weight: 600;
    font-size: 1rem;
}

/* Responsive Constraints */
@media (max-width: 1024px) {
    .hero-title-new { font-size: 2.8rem; }
}

@media (max-width: 992px) {
    .split-hero {
        flex-direction: column-reverse; /* Stack text below image normally, or image on top */
    }
    .hero-left, .hero-right {
        width: 100%;
    }
    .hero-right {
        height: 50vh;
        min-height: 400px;
    }
    .hero-image-full {
        position: relative;
    }
    .hero-left {
        padding: 60px 5%;
        min-height: auto;
    }
}

@media (max-width: 768px) {
    .hero-title-new { font-size: 2.2rem; }
    .hero-buttons-new { flex-direction: column; gap: 15px; }
    .btn-primary-solid, .btn-secondary-outline { width: 100%; text-align: center; }
    .hero-trust-new { gap: 20px; flex-direction: column; }
}
"""

with open(f"{base_dir}/styles.css", "a", encoding="utf-8") as f:
    f.write(new_css)

print("Hero section updated")
