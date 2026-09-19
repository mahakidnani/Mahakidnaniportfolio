from PIL import Image, ImageDraw, ImageFont

sizes = {
    'favicon.png': (64, 64),
    'apple-touch-icon.png': (180, 180),
}

for name, size in sizes.items():
    img = Image.new('RGBA', size, (10, 15, 26, 255))
    draw = ImageDraw.Draw(img)
    off = size[0] // 8
    draw.rectangle([off, off, size[0] - off, size[1] - off], outline=(91, 155, 213, 255), width=max(2, size[0] // 16))
    draw.line([off, size[1] - off, size[0] - off, off], fill=(91, 155, 213, 255), width=max(2, size[0] // 16))
    img.save(name)

Image.open('favicon.png').save('favicon.ico', sizes=[(64, 64)])

og = Image.new('RGB', (1200, 630), (10, 15, 26))
d = ImageDraw.Draw(og)
try:
    font = ImageFont.truetype('arial.ttf', 48)
except Exception:
    font = ImageFont.load_default()
d.text((80, 220), 'Mahak Idnani', fill=(232, 230, 225), font=font)
d.text((80, 310), 'Turning ambiguity into execution.', fill=(91, 155, 213), font=font)
og.save('og-image.png')
