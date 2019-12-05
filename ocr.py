import pytesseract
import extcolors
import requests
from PIL import ImageFilter
from PIL import Image
from PIL import ImageFont
from io import BytesIO

def process_image(img):
    print(_get_app(img))
    image = _get_image(img)
    image.filter(ImageFilter.SHARPEN)
    # Cabify = ((110, 91, 217), 1102)
    # Beat = ((35, 210, 171), 9345)
    # Uber = ((19, 19, 19), 355)
    # Satelital = ((193, 29, 27), 4045)
    # Indriver = ((22, 149, 44), 1780)
    #print(app)
    return pytesseract.image_to_string(image)
    #{
     #   data: pytesseract.image_to_string(image),
      #  color: colors[0].rgb
    #}

def _get_image(img):
    return Image.open(img)

def _get_app(img):
    name_colors = {
        'Cabify': ((110, 91, 217), 1102),
        'Beat': ((35, 210, 171), 9345),
        'Uber': ((19, 19, 19), 355),
        'Satelital': ((193, 29, 27), 4045),
        'Indriver': ((22, 149, 44), 1780)
    }
    colors = extcolors.extract(img)

    for i in colors[0]:
        print(i)
        if i == name_colors['Cabify'] :
            return 'Cabify'
        elif i == name_colors['Beat'] :
            return 'Beat'
        elif i == name_colors['Uber'] :
            return 'Uber'
        elif i == name_colors['Satelital'] :
            return 'Satelital'
        elif i == name_colors['Indriver'] :
            return 'Indriver'