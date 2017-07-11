import Image
import pytesseract
im = Image.open('a.jpg')
print pytesseract.image_to_string(im)

