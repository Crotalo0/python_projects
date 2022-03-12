# import image # image.py è nella stessa cartella
import image
import math
from datetime import datetime


def pixel_mapper(image_k, colorFunction):
    """function that accept color filters"""
    w = image_k.getWidth()
    h = image_k.getHeight()
    new_img = image.EmptyImage(w, h)
    for row in range(h):
        for col in range(w):
            oldpixel = image_k.getPixel(col, row)
            newpixel = colorFunction(oldpixel)
            new_img.setPixel(col, row, newpixel)
    return new_img


# grayscale func
def gray_scale(p):
    """grayScale filter for pixelMapper"""
    average = (p.getRed() + p.getGreen() + p.getBlue()) / 3
    newred = int(average)
    newgreen = int(average)
    newblue = int(average)
    newpixel = image.Pixel(newred, newgreen, newblue)
    return newpixel


def smooth(new_img):
    """smoothing pixelous images"""
    width = new_img.getWidth()
    height = new_img.getHeight()
    for row in range(height):
        for col in range(width):
            if row == 0 and col == 0:
                pixel1 = new_img.getPixel(col, row + 1)
                pixel2 = new_img.getPixel(col + 1, row)
                pixel3 = new_img.getPixel(col + 1, row + 1)
                R1 = int(pixel1.getRed())
                R2 = int(pixel2.getRed())
                R3 = int(pixel3.getRed())
                r_mean = int((R1 + R2 + R3) / 3)
                G1 = int(pixel1.getGreen())
                G2 = int(pixel2.getGreen())
                G3 = int(pixel3.getGreen())
                g_mean = int((G1 + G2 + G3) / 3)
                B1 = int(pixel1.getBlue())
                B2 = int(pixel2.getBlue())
                B3 = int(pixel3.getBlue())
                b_mean = int((B1 + B2 + B3) / 3)
                newpixel = image.Pixel(r_mean, g_mean, b_mean)
                new_img.setPixel(col, row, newpixel)
            elif row == 0 and col == (width - 1):
                pixel1 = new_img.getPixel(col - 1, row)
                pixel2 = new_img.getPixel(col - 1, row + 1)
                pixel3 = new_img.getPixel(col, row + 1)
                R1 = int(pixel1.getRed())
                R2 = int(pixel2.getRed())
                R3 = int(pixel3.getRed())
                r_mean = int((R1 + R2 + R3) / 3)
                G1 = int(pixel1.getGreen())
                G2 = int(pixel2.getGreen())
                G3 = int(pixel3.getGreen())
                g_mean = int((G1 + G2 + G3) / 3)
                B1 = int(pixel1.getBlue())
                B2 = int(pixel2.getBlue())
                B3 = int(pixel3.getBlue())
                b_mean = int((B1 + B2 + B3) / 3)
                newpixel = image.Pixel(r_mean, g_mean, b_mean)
                new_img.setPixel(col, row, newpixel)
            elif row == (height - 1) and col == 0:
                pixel1 = new_img.getPixel(col + 1, row)
                pixel2 = new_img.getPixel(col + 1, row - 1)
                pixel3 = new_img.getPixel(col, row - 1)
                R1 = int(pixel1.getRed())
                R2 = int(pixel2.getRed())
                R3 = int(pixel3.getRed())
                r_mean = int((R1 + R2 + R3) / 3)
                G1 = int(pixel1.getGreen())
                G2 = int(pixel2.getGreen())
                G3 = int(pixel3.getGreen())
                g_mean = int((G1 + G2 + G3) / 3)
                B1 = int(pixel1.getBlue())
                B2 = int(pixel2.getBlue())
                B3 = int(pixel3.getBlue())
                b_mean = int((B1 + B2 + B3) / 3)
                newpixel = image.Pixel(r_mean, g_mean, b_mean)
                new_img.setPixel(col, row, newpixel)
            elif row == (height - 1) and col == (width - 1):
                pixel1 = new_img.getPixel(col - 1, row)
                pixel2 = new_img.getPixel(col - 1, row - 1)
                pixel3 = new_img.getPixel(col, row - 1)
                R1 = int(pixel1.getRed())
                R2 = int(pixel2.getRed())
                R3 = int(pixel3.getRed())
                r_mean = int((R1 + R2 + R3) / 3)
                G1 = int(pixel1.getGreen())
                G2 = int(pixel2.getGreen())
                G3 = int(pixel3.getGreen())
                g_mean = int((G1 + G2 + G3) / 3)
                B1 = int(pixel1.getBlue())
                B2 = int(pixel2.getBlue())
                B3 = int(pixel3.getBlue())
                b_mean = int((B1 + B2 + B3) / 3)
                newpixel = image.Pixel(r_mean, g_mean, b_mean)
                new_img.setPixel(col, row, newpixel)
            elif row == 0 and 0 < col < (width - 1):
                pixel1 = new_img.getPixel(col - 1, row)
                pixel2 = new_img.getPixel(col + 1, row)
                pixel3 = new_img.getPixel(col, row + 1)
                pixel4 = new_img.getPixel(col - 1, row + 1)
                pixel5 = new_img.getPixel(col + 1, row + 1)
                R1 = int(pixel1.getRed())
                R2 = int(pixel2.getRed())
                R3 = int(pixel3.getRed())
                R4 = int(pixel4.getRed())
                R5 = int(pixel5.getRed())
                r_mean = int((R1 + R2 + R3 + R4 + R5) / 5)
                G1 = int(pixel1.getGreen())
                G2 = int(pixel2.getGreen())
                G3 = int(pixel3.getGreen())
                G4 = int(pixel4.getGreen())
                G5 = int(pixel5.getGreen())
                g_mean = int((G1 + G2 + G3 + G4 + G5) / 5)
                B1 = int(pixel1.getBlue())
                B2 = int(pixel2.getBlue())
                B3 = int(pixel3.getBlue())
                B4 = int(pixel4.getBlue())
                B5 = int(pixel5.getBlue())
                b_mean = int((B1 + B2 + B3 + B4 + B5) / 5)
                newpixel = image.Pixel(r_mean, g_mean, b_mean)
                new_img.setPixel(col, row, newpixel)
            elif row == (height - 1) and 0 < col < (width - 1):
                pixel1 = new_img.getPixel(col - 1, row)
                pixel2 = new_img.getPixel(col + 1, row)
                pixel3 = new_img.getPixel(col, row - 1)
                pixel4 = new_img.getPixel(col - 1, row - 1)
                pixel5 = new_img.getPixel(col + 1, row - 1)
                R1 = int(pixel1.getRed())
                R2 = int(pixel2.getRed())
                R3 = int(pixel3.getRed())
                R4 = int(pixel4.getRed())
                R5 = int(pixel5.getRed())
                r_mean = int((R1 + R2 + R3 + R4 + R5) / 5)
                G1 = int(pixel1.getGreen())
                G2 = int(pixel2.getGreen())
                G3 = int(pixel3.getGreen())
                G4 = int(pixel4.getGreen())
                G5 = int(pixel5.getGreen())
                g_mean = int((G1 + G2 + G3 + G4 + G5) / 5)
                B1 = int(pixel1.getBlue())
                B2 = int(pixel2.getBlue())
                B3 = int(pixel3.getBlue())
                B4 = int(pixel4.getBlue())
                B5 = int(pixel5.getBlue())
                b_mean = int((B1 + B2 + B3 + B4 + B5) / 5)
                newpixel = image.Pixel(r_mean, g_mean, b_mean)
                new_img.setPixel(col, row, newpixel)
            elif 0 < row < (height - 1) and col == 0:
                pixel1 = new_img.getPixel(col, row - 1)
                pixel2 = new_img.getPixel(col + 1, row - 1)
                pixel3 = new_img.getPixel(col + 1, row)
                pixel4 = new_img.getPixel(col, row + 1)
                pixel5 = new_img.getPixel(col + 1, row + 1)
                R1 = int(pixel1.getRed())
                R2 = int(pixel2.getRed())
                R3 = int(pixel3.getRed())
                R4 = int(pixel4.getRed())
                R5 = int(pixel5.getRed())
                r_mean = int((R1 + R2 + R3 + R4 + R5) / 5)
                G1 = int(pixel1.getGreen())
                G2 = int(pixel2.getGreen())
                G3 = int(pixel3.getGreen())
                G4 = int(pixel4.getGreen())
                G5 = int(pixel5.getGreen())
                g_mean = int((G1 + G2 + G3 + G4 + G5) / 5)
                B1 = int(pixel1.getBlue())
                B2 = int(pixel2.getBlue())
                B3 = int(pixel3.getBlue())
                B4 = int(pixel4.getBlue())
                B5 = int(pixel5.getBlue())
                b_mean = int((B1 + B2 + B3 + B4 + B5) / 5)
                newpixel = image.Pixel(r_mean, g_mean, b_mean)
                new_img.setPixel(col, row, newpixel)
            elif 0 < row < (height - 1) and col == (width - 1):
                pixel1 = new_img.getPixel(col, row - 1)
                pixel2 = new_img.getPixel(col - 1, row - 1)
                pixel3 = new_img.getPixel(col - 1, row)
                pixel4 = new_img.getPixel(col, row + 1)
                pixel5 = new_img.getPixel(col - 1, row + 1)
                R1 = int(pixel1.getRed())
                R2 = int(pixel2.getRed())
                R3 = int(pixel3.getRed())
                R4 = int(pixel4.getRed())
                R5 = int(pixel5.getRed())
                r_mean = int((R1 + R2 + R3 + R4 + R5) / 5)
                G1 = int(pixel1.getGreen())
                G2 = int(pixel2.getGreen())
                G3 = int(pixel3.getGreen())
                G4 = int(pixel4.getGreen())
                G5 = int(pixel5.getGreen())
                g_mean = int((G1 + G2 + G3 + G4 + G5) / 5)
                B1 = int(pixel1.getBlue())
                B2 = int(pixel2.getBlue())
                B3 = int(pixel3.getBlue())
                B4 = int(pixel4.getBlue())
                B5 = int(pixel5.getBlue())
                b_mean = int((B1 + B2 + B3 + B4 + B5) / 5)
                newpixel = image.Pixel(r_mean, g_mean, b_mean)
                new_img.setPixel(col, row, newpixel)
            else:
                pixel1 = new_img.getPixel(col - 1, row - 1)
                pixel2 = new_img.getPixel(col - 1, row)
                pixel3 = new_img.getPixel(col - 1, row + 1)
                pixel4 = new_img.getPixel(col, row + 1)
                pixel5 = new_img.getPixel(col, row - 1)
                pixel6 = new_img.getPixel(col + 1, row)
                pixel7 = new_img.getPixel(col + 1, row + 1)
                pixel8 = new_img.getPixel(col + 1, row - 1)
                R1 = int(pixel1.getRed())
                R2 = int(pixel2.getRed())
                R3 = int(pixel3.getRed())
                R4 = int(pixel4.getRed())
                R5 = int(pixel5.getRed())
                R6 = int(pixel6.getRed())
                R7 = int(pixel7.getRed())
                R8 = int(pixel8.getRed())
                r_mean = int((R1 + R2 + R3 + R4 + R5 + R6 + R7 + R8) / 8)
                G1 = int(pixel1.getGreen())
                G2 = int(pixel2.getGreen())
                G3 = int(pixel3.getGreen())
                G4 = int(pixel4.getGreen())
                G5 = int(pixel5.getGreen())
                G6 = int(pixel6.getGreen())
                G7 = int(pixel7.getGreen())
                G8 = int(pixel8.getGreen())
                g_mean = int((G1 + G2 + G3 + G4 + G5 + G6 + G7 + G8) / 8)
                B1 = int(pixel1.getBlue())
                B2 = int(pixel2.getBlue())
                B3 = int(pixel3.getBlue())
                B4 = int(pixel4.getBlue())
                B5 = int(pixel5.getBlue())
                B6 = int(pixel6.getBlue())
                B7 = int(pixel7.getBlue())
                B8 = int(pixel8.getBlue())
                b_mean = int((B1 + B2 + B3 + B4 + B5 + B6 + B7 + B8) / 8)
                newpixel = image.Pixel(r_mean, g_mean, b_mean)
                new_img.setPixel(col, row, newpixel)
    return new_img


def sobel(oldimage):
    """Try on sobel edge detector algorhythm if image is really pixelous"""
    # Applying some info I took there (and wikipedia):
    # https://www.projectrhea.org/rhea/index.php/An_Implementation_of_Sobel_Edge_Detection

    # first grayScale to image.
    new_image = pixel_mapper(oldimage, gray_scale)
    w = new_image.getWidth()
    h = new_image.getHeight()
    new_img = image.EmptyImage(w, h)
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            Gx = 0
            Gy = 0

            pixel1 = new_image.getPixel(col - 1, row - 1)  # top-left
            pixel2 = new_image.getPixel(col - 1, row)  # left
            pixel3 = new_image.getPixel(col - 1, row + 1)  # bottom-left
            pixel4 = new_image.getPixel(col, row - 1)  # top
            pixel5 = new_image.getPixel(col, row + 1)  # bottom
            pixel6 = new_image.getPixel(col + 1, row - 1)  # top-right
            pixel7 = new_image.getPixel(col + 1, row)  # right
            pixel8 = new_image.getPixel(col + 1, row + 1)  # bottom-right

            R1 = int(pixel1.getRed())
            R2 = int(pixel2.getRed())
            R3 = int(pixel3.getRed())
            R4 = int(pixel4.getRed())
            R5 = int(pixel5.getRed())
            R6 = int(pixel6.getRed())
            R7 = int(pixel7.getRed())
            R8 = int(pixel8.getRed())

            G1 = int(pixel1.getGreen())
            G2 = int(pixel2.getGreen())
            G3 = int(pixel3.getGreen())
            G4 = int(pixel4.getGreen())
            G5 = int(pixel5.getGreen())
            G6 = int(pixel6.getGreen())
            G7 = int(pixel7.getGreen())
            G8 = int(pixel8.getGreen())

            B1 = int(pixel1.getBlue())
            B2 = int(pixel2.getBlue())
            B3 = int(pixel3.getBlue())
            B4 = int(pixel4.getBlue())
            B5 = int(pixel5.getBlue())
            B6 = int(pixel6.getBlue())
            B7 = int(pixel7.getBlue())
            B8 = int(pixel8.getBlue())

            intensity1 = R1 + G1 + B1
            Gx += +intensity1
            Gy += +intensity1
            intensity2 = R2 + G2 + B2
            Gx += +2 * intensity2
            Gy += 0
            intensity3 = R3 + G3 + B3
            Gx += +intensity3
            Gy += -intensity3
            intensity4 = R4 + G4 + B4
            Gx += 0
            Gy += 2 * intensity4
            intensity5 = R5 + G5 + B5
            Gx += 0
            Gy += -2 * intensity5
            intensity6 = R6 + G6 + B6
            Gx += -intensity6
            Gy += +intensity6
            intensity7 = R7 + G7 + B7
            Gx += -2 * intensity7
            Gy += 0
            intensity8 = R8 + G8 + B8
            Gx += -intensity8
            Gy += -intensity8

            length = math.sqrt((Gx * Gx) + (Gy * Gy))
            length = length / 4328 * 255
            length = int(length)
            newpixel = image.Pixel(length, length, length)
            new_img.setPixel(col, row, newpixel)

    return new_img


def sobel_smooth(oldimage):
    """Try on sobel edge detector algorhythm if image is really pixelous"""
    # Applying some info I took there (and wikipedia):
    # https://www.projectrhea.org/rhea/index.php/An_Implementation_of_Sobel_Edge_Detection

    # first smooth the image then apply grayScale.
    new = smooth(oldimage)
    new_image = pixel_mapper(new, gray_scale)
    w = new_image.getWidth()
    h = new_image.getHeight()
    new_img = image.EmptyImage(w, h)
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            Gx = 0
            Gy = 0

            pixel1 = new_image.getPixel(col - 1, row - 1)  # top-left
            pixel2 = new_image.getPixel(col - 1, row)  # left
            pixel3 = new_image.getPixel(col - 1, row + 1)  # bottom-left
            pixel4 = new_image.getPixel(col, row - 1)  # top
            pixel5 = new_image.getPixel(col, row + 1)  # bottom
            pixel6 = new_image.getPixel(col + 1, row - 1)  # top-right
            pixel7 = new_image.getPixel(col + 1, row)  # right
            pixel8 = new_image.getPixel(col + 1, row + 1)  # bottom-right

            R1 = int(pixel1.getRed())
            R2 = int(pixel2.getRed())
            R3 = int(pixel3.getRed())
            R4 = int(pixel4.getRed())
            R5 = int(pixel5.getRed())
            R6 = int(pixel6.getRed())
            R7 = int(pixel7.getRed())
            R8 = int(pixel8.getRed())

            G1 = int(pixel1.getGreen())
            G2 = int(pixel2.getGreen())
            G3 = int(pixel3.getGreen())
            G4 = int(pixel4.getGreen())
            G5 = int(pixel5.getGreen())
            G6 = int(pixel6.getGreen())
            G7 = int(pixel7.getGreen())
            G8 = int(pixel8.getGreen())

            B1 = int(pixel1.getBlue())
            B2 = int(pixel2.getBlue())
            B3 = int(pixel3.getBlue())
            B4 = int(pixel4.getBlue())
            B5 = int(pixel5.getBlue())
            B6 = int(pixel6.getBlue())
            B7 = int(pixel7.getBlue())
            B8 = int(pixel8.getBlue())

            intensity1 = R1 + G1 + B1
            Gx += +intensity1
            Gy += +intensity1
            intensity2 = R2 + G2 + B2
            Gx += +2 * intensity2
            Gy += 0
            intensity3 = R3 + G3 + B3
            Gx += +intensity3
            Gy += -intensity3
            intensity4 = R4 + G4 + B4
            Gx += 0
            Gy += 2 * intensity4
            intensity5 = R5 + G5 + B5
            Gx += 0
            Gy += -2 * intensity5
            intensity6 = R6 + G6 + B6
            Gx += -intensity6
            Gy += +intensity6
            intensity7 = R7 + G7 + B7
            Gx += -2 * intensity7
            Gy += 0
            intensity8 = R8 + G8 + B8
            Gx += -intensity8
            Gy += -intensity8

            length = math.sqrt((Gx * Gx) + (Gy * Gy))
            length = length / 4328 * 255
            length = int(length)
            newpixel = image.Pixel(length, length, length)
            new_img.setPixel(col, row, newpixel)

    return new_img


img = image.Image("solaireshield.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
local_time = datetime.now()
print("starting...", local_time)
final = sobel(img)
final.draw(win)
final.save("sobeled.jpg")

local_time1 = datetime.now()
print("...finished! In: ", local_time1 - local_time)

win.exitonclick()
