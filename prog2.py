import pyttsx
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',rate-30)
engine.say('just one word')
engine.runAndWait()
