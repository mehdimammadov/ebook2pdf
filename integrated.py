#box coordinates of the book X1,Y1,X2,Y2
X1,Y1,X2,Y2 = 3190, 190, 4640, 1940

#next button position
X3, Y3 = 5655, 1045

#mousemove delay in millisec (if needed)
delay = 0

#nuber of pages or slides (number of mouse clicks)
pages = 817

#path to folder
path = '/home/mehanton/Documents/Python/screenshot/images/'

import pyscreenshot as ImageGrab
import pyautogui
import time

ext = '.png'

for i in range(pages):
    im = ImageGrab.grab(bbox=(X1,Y1,X2,Y2))  # X1,Y1,X2,Y23
    # #show the image
    # im.show()

    im.save(path + str(i+1) + ext)
    pyautogui.click(x=5655, y=1045, interval=0.25)
    time.sleep(1)

