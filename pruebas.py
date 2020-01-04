from PIL import Image
from PIL import EpsImagePlugin

filename = 'cabify.jpeg'
def open_eps(filename, dpi):
    img = Image.open(filename)
    print(img)
    original = [float(d) for d in img.size]
    # scale = width / original[0] # calculated wrong height
    scale = dpi/72.0            # this fixed it
    if dpi is not 0:
        img.load(int(scale))
    if scale != 1:
        img.thumbnail([round(scale * d) for d in original], Image.ANTIALIAS)
    return img

img = open_eps(filename, 300.0)
img.save('cabify1.png', (300.0, 300.0))