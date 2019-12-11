import pytesseract
import extcolors
import requests
from PIL import ImageFilter
from PIL import Image
from PIL import ImageFont
from io import BytesIO

def process_image(img):
  image = _get_image(img)
  image.filter(ImageFilter.SHARPEN)
  # Cabify = ((110, 91, 217), 1102)
  # Beat = ((35, 210, 171), 9345)
  # Uber = ((19, 19, 19), 355)
  # Satelital = ((193, 29, 27), 4045)
  # Indriver = ((22, 149, 44), 1780)
  # pytesseract.image_to_string(image)
  # print(_get_app(image))
  return _get_app(image)
  #{
    #   data: pytesseract.image_to_string(image),
    #  color: colors[0].rgb
  #}

def _get_image(img):
  return Image.open(BytesIO(requests.get(img).content))

def _get_app(image):
  lista_strings = pytesseract.image_to_string(image).split()
  new_lista = []

  for string in lista_strings: 
    if string == 'Easy':
      new_lista.append(['easy', lista_strings.index(string)])
    elif string == 'Lite':
      new_lista.append(['lite', lista_strings.index(string)])
    elif string == 'Executive': 
      new_lista.append(['executive', lista_strings.index(string)])

  category_cabify = [
    _get_data(new_lista[0][0], lista_strings[new_lista[0][1]:new_lista[1][1]]),
    _get_data(new_lista[1][0], lista_strings[new_lista[1][1]:new_lista[2][1]]),
    _get_data(new_lista[2][0], lista_strings[new_lista[2][1]:])
  ]

  # filter_string = list(filter(lambda string: string == 'Lite', lista_strings))
  return category_cabify


def _get_data(category, lista):
  new_array = [
    ['categoria ' + category],
    _get_price(lista),
    _get_time(lista)
  ]
  return new_array

def _get_price(lista):
  for string in lista:
    for idx, x in enumerate(string):
      if x == 'S' or x == '$':
        return ['precio ' + string.replace('$/', 'S/.')]

def _get_time(lista):
  for string in lista:
    for i, x in enumerate(string):
      if x == 'm':
        if string[i + 1] == 'i':
          return ['tiempo '+ lista[lista.index(string) - 1] + ' min']