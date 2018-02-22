#!/usr/bin/python3
from wand.image import Image


def modify(img):
    with img.clone() as i:
        i.crop(i.width // 2 - min(int(i.width), int(i.height)) // 2, i.height // 2 - min(int(i.width), int(i.height)) // 2, width=min(int(i.width), int(i.height)), height=min(int(i.width), int(i.height)))
        print(i.depth)
        i.sample(128,128)
        i.sample(1024,1024)
        i.format = 'png'
        print("Image resized.")
        img_bin = i.make_blob()
    return img_bin


def load(imgloc):
    img = Image(filename=imgloc)
    print("Image loaded.")
    return img


def write(img):
    with open('output.png', 'wb') as f:
        f.write(img)
    print("Image written.")
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
