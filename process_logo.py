import os
from PIL import Image

brain_dir = r"C:\Users\Panchakshari S H\.gemini\antigravity\brain\327eba55-685f-46f4-b441-5a1cccc949f9"
img_path = os.path.join(brain_dir, "media__1776003005995.jpg")

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"
logo_path = os.path.join(base_dir, "logo.png")
favicon_path = os.path.join(base_dir, "favicon.ico")

# Open original image
img = Image.open(img_path)

# Convert to RGBA for transparent background capability if needed, though it's a JPG so it's probably have white bg
img = img.convert("RGBA")

width, height = img.size

# Look at the user's logo attachment: the top 70-75% is the circular logo, the bottom 25-30% is the text
crop_height = int(height * 0.65) # Approx where the text starts
crop_box = (0, 0, width, crop_height)
logo_crop = img.crop(crop_box)

# Try to make the white background transparent (simple approach)
datas = logo_crop.getdata()
newData = []
for item in datas:
    # If the pixel is very close to white, make it transparent
    if item[0] > 240 and item[1] > 240 and item[2] > 240:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

logo_crop.putdata(newData)

# Crop out any excessive transparent boundary (bbox)
bbox = logo_crop.getbbox()
if bbox:
    logo_crop = logo_crop.crop(bbox)

# Save high res for navbar
logo_crop.save(logo_path, "PNG")

# Create a square favicon out of it
w, h = logo_crop.size
max_dim = max(w, h)
favicon_canvas = Image.new("RGBA", (max_dim, max_dim), (255, 255, 255, 0))
favicon_canvas.paste(logo_crop, ((max_dim - w) // 2, (max_dim - h) // 2))

favicon_resized = favicon_canvas.resize((64, 64), Image.Resampling.LANCZOS)
favicon_resized.save(favicon_path, format="ICO", sizes=[(64, 64)])

print("Logo and Favicon perfectly generated!")
