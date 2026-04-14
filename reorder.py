import re
import os

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

with open(f"{base_dir}/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# I will use a simple logical split based on the <section tags.

# 1. Grab everything from <section id="gallery" up to <section id="contact"
# Wait, <section id="contact" comes right after testimonials.
# So I want to extract [ gallery -> teachers -> testimonials ]
block_match = re.search(r'(<section id="gallery".*?<section id="contact")', html, re.DOTALL)
if block_match:
    moving_blocks = block_match.group(1)
    # The moving_blocks ends right before <section id="contact", so we must NOT include <section id="contact" in moving_blocks.
    # Ah, the regex captures up to the START of <section id="contact". Wait, .*? stops before it due to the match.
    # Actually, re.search returns the match which INCLUDES the <section id="contact" string.
    pass

# Better approach: string splitting
def extract_section(html_str, section_id):
    # Find start
    start_tag = f'<section id="{section_id}"'
    start_idx = html_str.find(start_tag)
    if start_idx == -1: return ""
    
    # By searching for the next <section or <footer to find the end
    part = html_str[start_idx:]
    next_tag = part.find('<section id=', 1)
    if next_tag == -1:
        next_tag = part.find('<footer')
        
    if next_tag != -1:
        return part[:next_tag]
    return part

block_gallery = extract_section(html, "gallery")
block_teachers = extract_section(html, "teachers")
block_testimonials = extract_section(html, "testimonials")

combined_moving_blocks = block_gallery + block_teachers + block_testimonials

# Delete them from original
html = html.replace(block_gallery, '')
html = html.replace(block_teachers, '')
html = html.replace(block_testimonials, '')

# Now insert them BEFORE <section id="courses"
courses_idx = html.find('<section id="courses"')
if courses_idx != -1:
    html = html[:courses_idx] + combined_moving_blocks + html[courses_idx:]

# Also update the navbar!
nav_match = re.search(r'(<ul class="nav-links">.*?</ul>)', html, re.DOTALL)
if nav_match:
    old_nav = nav_match.group(1)
    new_nav = """<ul class="nav-links">
                <li><a href="#home" class="nav-link">Home</a></li>
                <li><a href="#about" class="nav-link">About Us</a></li>
                <li><a href="#gallery" class="nav-link">Gallery</a></li>
                <li><a href="#teachers" class="nav-link">Teachers</a></li>
                <li><a href="#testimonials" class="nav-link">Testimonials</a></li>
                <li><a href="#courses" class="nav-link">Courses</a></li>
                <li><a href="#events" class="nav-link">Events</a></li>
                <li><a href="#contact" class="nav-link">Contact</a></li>
            </ul>"""
    html = html.replace(old_nav, new_nav)

with open(f"{base_dir}/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Sections successfully rearranged.")
