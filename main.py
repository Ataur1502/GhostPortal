from PIL import Image

img = Image.open("challenge.png").convert("RGBA")

width, height = img.size
out = Image.new("L", (width, height))

pixels = img.load()
out_pixels = out.load()

for y in range(height):
    for x in range(width):
        _, _, _, a = pixels[x, y]

        if a & 1:
            out_pixels[x, y] = 0      # Black
        else:
            out_pixels[x, y] = 255    # White

out.save("recovered_qr.png")
print("Saved recovered_qr.png")