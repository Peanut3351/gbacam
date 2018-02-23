#!/usr/bin/python3
import PIL.Image as Image
import png
import numpy as np


def modify(img):
    i = img.point(lambda x: int(x/17))
    #i.mode = 'L;4'
    width, height = img.size
    i.crop((img.size[0] // 2 - min(width, height) // 2, img.size[1] // 2 - min(width, height) // 2, min(width, height), min(width, height)))
    i.resize((128,128))
    i.resize((1024,1024))
    print("Image resized.")
    return i


def load(imgloc):
    img = Image.open(imgloc)
    print("Image loaded.")
    return img


def write(img):
    png.from_array(np.asarray(img, np.uint8), 'L;4').save('output.png')
    #img.save('output.png')
    print("Image written.")
    return


def getInput():
    imgloc = input("Please enter the location of your image: ")
    return imgloc


def run():
    imgloc = str(getInput())
    img = load(imgloc)
    imgmod = modify(img)
    write(imgmod)
    print("Your image can be found in the directory of this program.")
    rerun = input("Run again? (y/n) ")
    while True:
        if rerun.lower() == "y" or rerun.lower() == "yes":
            run()
            break
        if rerun.lower() == "n" or rerun.lower() == "no":
            print("Thanks for using gbacam!")
            exit()
        print("Error, not a valid input.")
    return


print("Welcome to gbacam")
run()
