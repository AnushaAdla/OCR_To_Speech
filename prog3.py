import Image
import pyttsx
import pytesseract
im = Image.open('a.jpg')
print pytesseract.image_to_string(im)
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',rate-30)

engine.say(pytesseract.image_to_string(im))
engine.runAndWait()
