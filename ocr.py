import pytesseract
import requests
from PIL import ImageFilter
from PIL import Image
from io import BytesIO

def process_image(img):
    image = _get_image(img)
    image.filter(ImageFilter.SHARPEN)
    return pytesseract.image_to_string(image)

def _get_image(img):
    return Image.open(img)