"""
This script is garbage and will most likely not work on different computers
"""

import glob
import constants
from PIL import Image
import math


DIMENSIONS = {
    "A4": [8.27, 11.69],
    "A3": [11.69, 16.53]
}

desired_dim = DIMENSIONS["A4"]


def circ(im, radius):
    x, y = im.size
    centerx, centery = x // 2, y // 2
    data = im.load()
    for i in range(x):
        for j in range(y):
            dist = math.sqrt((i - centerx) ** 2 + (j - centery) ** 2)
            if dist > radius:
                data[i, j] = (0, 0, 0)


def paste(source_data, to, offset):
    data = to.load()
    x, y = to.size
    xoffset, yoffset = offset
    for xidx in range(x):
        for yidx in range(y):
            source_data[xoffset + xidx, yoffset + yidx] = data[xidx, yidx]


def create_image(data):
    size = (int(desired_dim[0] * 96), int(desired_dim[1] * 96))
    stiched_image = Image.new("RGB", size, "white")
    stiched_image_data = stiched_image.load()
    try:
        print(data)
        total = 0
        idx = 0
        idy = 0

        for monster, monster_size in data:
            # open the monster image
            monster_im = Image.open(monster)
            monster_im.thumbnail((96, 96), Image.ANTIALIAS)
            circ(monster_im, 46)
            xpos = idx * 96
            if xpos + monster_im.width + 30 > stiched_image.width:
                idy += 1
                idx = 0
                xpos = 0
            ypos = idy * 96
            idx += 1
            print("x", xpos, "y", ypos, "source size", stiched_image.size)
            paste(stiched_image_data, monster_im, (xpos, ypos))
            total += 96
        stiched_image.show()
        stiched_image.save("~/Desktop/save.png")
    except Exception:
        print("Error")
        stiched_image.show()
        stiched_image.save(constants.DATA_DIR + "/out.png")


def main():
    path = constants.TOKEN_DIR + "/*"
    files = glob.glob(path)
    enumerated = list(enumerate(files))
    print("enter all the tokens you want to include.")
    data = []
    while True:
        print("showing available files")
        for idx, f in enumerated:
            print("(" + str(idx) + ")", f[f.rfind("/") + 1:])
        print("press '!' to exit")
        answer = input(":")
        if answer == "!":
            break
        else:
            try:
                x = int(answer)
                creature = enumerated[x][1]
                print("added: ", creature)
                #size = input("size of the creature? (H)uge (L)arge, (N)ormal (S)mall")
                #if not ("L" in size or "N" in size or "S" in size or "H" in size.upper()):
                #    raise Exception("unknown size")
                times = int(input("how many tiems should this token be included? "))
                for _ in range(times):
                    data += [(creature, "N")]
            except:
                print("error")
    create_image(data)


if __name__ == '__main__':
    main()
