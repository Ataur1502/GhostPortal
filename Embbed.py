from PIL import Image

# Load images
profile = Image.open("employee.png").convert("RGBA")
qr = Image.open("qrcode.png").convert("L")

# Resize QR to fit
qr = qr.resize(profile.size)

pixels = profile.load()
qr_pixels = qr.load()

width, height = profile.size

for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]

        # QR: black -> 1, white -> 0
        bit = 1 if qr_pixels[x, y] < 128 else 0

        # Store in alpha LSB
        a = (a & 0xFE) | bit

        pixels[x, y] = (r, g, b, a)

profile.save("challenge.png")
print("Saved challenge.png")