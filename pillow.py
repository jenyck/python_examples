import math
from PIL import Image, ImageDraw


def swap(img, x0, y0, x1, y1, width):
    new_img = img.copy()
    section1 = new_img.crop((x0, y0, x0 + width, y0 + width))
    section2 = new_img.crop((x1, y1, x1 + width, y1 + width))
    section1 = section1.rotate(-90, expand=True)
    section2 = section2.rotate(-90, expand=True)

    new_img.paste(section1, (x1, y1))
    new_img.paste(section2, (x0, y0))
    new_img = new_img.rotate(-90, expand=True)

    return new_img


def avg_color(img, x0, y0, x1, y1):
    new_img = img.copy()
    width, height = img.size
    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            avg = [0, 0, 0]
            count = 0
            neighbours = [(x, y-1), (x, y+1),
                          (x-1, y-1), (x-1, y), (x-1, y+1),
                          (x+1, y-1), (x+1, y), (x+1, y+1)]
            for dot in neighbours:
                if (0 <= dot[0] < width) and (0 <= dot[1] < height):
                    color = img.getpixel(dot)
                    avg[0] += color[0]
                    avg[1] += color[1]
                    avg[2] += color[2]
                    count += 1
            new_color = (int(avg[0]/count),
                         int(avg[1]/count),
                         int(avg[2]/count))
            new_img.putpixel((x, y), new_color)
    return new_img


def pentagram(img, x, y, r, thickness, color):
    draw = ImageDraw.Draw(img)
    points = []
    color = tuple(color)

    for i in range(5):
        phi = (math.pi / 5) * (2 * i + 3 / 2)
        node_i = (int(x + r * math.cos(phi)), int(y + r * math.sin(phi)))
        points.append(node_i)

    draw.line([points[0], points[2]], fill=color, width=thickness)
    draw.line([points[2], points[4]], fill=color, width=thickness)
    draw.line([points[4], points[1]], fill=color, width=thickness)
    draw.line([points[1], points[3]], fill=color, width=thickness)
    draw.line([points[3], points[0]], fill=color, width=thickness)

    draw.ellipse((x - r, y - r, x + r, y + r), outline=color, width=thickness)

    return imgimport math
from PIL import Image, ImageDraw


def swap(img, x0, y0, x1, y1, width):
    new_img = img.copy()
    section1 = new_img.crop((x0, y0, x0 + width, y0 + width))
    section2 = new_img.crop((x1, y1, x1 + width, y1 + width))
    section1 = section1.rotate(-90, expand=True)
    section2 = section2.rotate(-90, expand=True)

    new_img.paste(section1, (x1, y1))
    new_img.paste(section2, (x0, y0))
    new_img = new_img.rotate(-90, expand=True)

    return new_img


def avg_color(img, x0, y0, x1, y1):
    new_img = img.copy()
    width, height = img.size
    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            avg = [0, 0, 0]
            count = 0
            neighbours = [(x, y-1), (x, y+1),
                          (x-1, y-1), (x-1, y), (x-1, y+1),
                          (x+1, y-1), (x+1, y), (x+1, y+1)]
            for dot in neighbours:
                if (0 <= dot[0] < width) and (0 <= dot[1] < height):
                    color = img.getpixel(dot)
                    avg[0] += color[0]
                    avg[1] += color[1]
                    avg[2] += color[2]
                    count += 1
            new_color = (int(avg[0]/count),
                         int(avg[1]/count),
                         int(avg[2]/count))
            new_img.putpixel((x, y), new_color)
    return new_img


def pentagram(img, x, y, r, thickness, color):
    draw = ImageDraw.Draw(img)
    points = []
    color = tuple(color)

    for i in range(5):
        phi = (math.pi / 5) * (2 * i + 3 / 2)
        node_i = (int(x + r * math.cos(phi)), int(y + r * math.sin(phi)))
        points.append(node_i)

    draw.line([points[0], points[2]], fill=color, width=thickness)
    draw.line([points[2], points[4]], fill=color, width=thickness)
    draw.line([points[4], points[1]], fill=color, width=thickness)
    draw.line([points[1], points[3]], fill=color, width=thickness)
    draw.line([points[3], points[0]], fill=color, width=thickness)

    draw.ellipse((x - r, y - r, x + r, y + r), outline=color, width=thickness)

    return img
