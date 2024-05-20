# how this works...
# basically, it takes a screenshot of the full screen every 60 sec, parses all the text from it,
# if the text that you want is there it will call the function that you can customize
# works on mac, windows and prob linux (im on mac so i cant test windows or linux)

import os
import pytesseract
from PIL import Image
import time

# the text that will trigger the bot
textToDetect = "Flash Giveaway"

# the less you put, the more accurate the bot will be but the performance will suffer
secBetweenChecks = 60

# insert your code here to actually let you know that the text has been detected
def foundTextInImg():
    print("FLASH GIVEAWAY!!")


# this is a simple script that will detect whatever text you want on the screen
while True:
    os.system("screencapture screen.png")
    image = Image.open('screen.png')
    text = pytesseract.image_to_string(image)
    if textToDetect in text:
        foundTextInImg()
        break
    os.remove("screen.txt")
    time.sleep(secBetweenChecks)
