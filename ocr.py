import pytesseract
import extcolors
import requests
from PIL import ImageFilter
from PIL import Image
from io import BytesIO

def process_image(img):
    image = _get_image(img)
    image.filter(ImageFilter.SHARPEN)
    colors = extcolors.extract(img)
    # Cabify = ((110, 91, 217), 1102)
    # Beat = ((35, 210, 171), 9345)
    # Uber = ((19, 19, 19), 355)
    # Satelital = ((193, 29, 27), 4045)
    # Indriver = ((22, 149, 44), 1780)
    print(colors[0])
    return pytesseract.image_to_string(image)
    #{ 
     #   data: pytesseract.image_to_string(image), 
      #  color: colors[0].rgb
    #}

def _get_image(img):
    return Image.open(img)