import os
import pytesseract
from PIL import Image
import time


# insert your code here to actually let you know that the text has been detected
def foundTextInImg():
    print("FLASH GIVEAWAY!!")


# this is a simple script that will detect whatever text you want on the screen
textToDetect = "Flash Giveaway"
while True:
    os.system("screencapture screen.png")
    image = Image.open('screen.png')
    text = pytesseract.image_to_string(image)
    if textToDetect in text:
        foundTextInImg()
        break
    os.remove("screen.txt")
    time.sleep(60)
