#!/usr/bin/python3
import time
from wand.image import Image
from wand.display import display


def modify(img):
    with img.clone() as i:
        i.crop()
    return i


def load(imgloc):
    img = Image(filename=imgloc)
    return img


def write(img):
    return


def getInput():
    imgloc = input("Please enter the location of your image: ")
    return imgloc


def getHelp():
    return


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
