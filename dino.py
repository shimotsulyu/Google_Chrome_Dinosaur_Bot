import pyautogui
from PIL import ImageGrab, ImageOps
from numpy import *

replay = (915, 336)
dino = (624, 343)

def imagegrab():
    x, y, a, b = 665, 338, 50, 30
    box = (x,y,x+a,y+b)
    img = ImageGrab.grab(box)
    gray = ImageOps.grayscale(img)
    a = sum(array(gray.getcolors()))
    print(a)
    return a

def restart():
    pyautogui.click(replay)

def main():
    restart()
    while True:
        imagegrab()
        if (imagegrab() != 1747):
            pyautogui.press('space')

if __name__ == "__main__":
    main()