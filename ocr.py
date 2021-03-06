import pytesseract
import extcolors
import requests
import base64

from PIL import ImageFilter
from PIL import Image
from PIL import ImageFont
from io import BytesIO

from cabify import cabify
from beat import beat
from uber import uber
from satelital import satelital

def process_image(img):
  image = _get_image(img)
  # print(image.size)
  image.filter(ImageFilter.SHARPEN)
  # Cabify = ((110, 91, 217), 1102)
  # Beat = ((35, 210, 171), 9345)
  # Uber = ((19, 19, 19), 355)
  # Satelital = ((193, 29, 27), 4045)
  # Indriver = ((22, 149, 44), 1780)
  lista_strings = pytesseract.image_to_string(image).split()
  # print(lista_strings)
  return get_category(lista_strings)

def _get_image(img):
  return Image.open(BytesIO(base64.b64decode(img)))

def get_category(lista_strings):
  for string in lista_strings:
    if string == 'Easy':
      return cabify(lista_strings)
    elif string == 'BEAT':
      return beat(lista_strings)
    elif string == 'UberX':
      return uber(lista_strings)
    elif string == '(Estimado)':
      return satelital(lista_strings)
