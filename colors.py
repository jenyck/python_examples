#!/usr/bin/env python3
from PIL import Image


# write your function here
def getcolors(source_img, maxcolors):
    colors = dict()
    width, height = source_img.size
    for x in range(width):
        for y in range(height):
            pix = source_img.getpixel((x, y))
            if pix not in colors.keys():
                if len(colors.keys()) < maxcolors:
                    colors[pix] = 1
            else:
                colors[pix] += 1
    result = []
    for i in colors.keys():
        result.append((colors[i], i))
    return result

source_img = Image.new("RGB", (500, 100), 'black')
img1 = Image.new("RGB", (10, 30), 'red')
img2 = Image.new("RGB", (10, 20), 'blue')
img3 = Image.new("RGB", (10, 20), 'yellow')
source_img.paste(img1, (200, 50))
source_img.paste(img2, (100, 80))
source_img.paste(img3, (50, 20))

print(getcolors(source_img, 3))
