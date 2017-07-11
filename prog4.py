import Image
import sys
import pyttsx
import pytesseract
im = Image.open(open(sys.argv[1]))
fp = open("pre.txt","wb")
fp.write(pytesseract.image_to_string(im))
engine = pyttsx.init()
fp.close()
rate = engine.getProperty('rate')
engine.setProperty('rate',rate-50)
fp = open("pre.txt","r+")
thetext = fp.read()
fp.close()
engine.say(thetext)
engine.runAndWait()

