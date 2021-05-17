"""
This program loads an image and applies the narok filter
to it by setting "bright" pixels to grayscale values.
"""

from simpleimage import SimpleImage

BRIGHT_THRESHOLD = 153

def main():
    image = SimpleImage('images/simba-sq.jpg')
    for pixel in image:
        pixel_avg = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel_avg > BRIGHT_THRESHOLD:
            # set to grayscale
            pixel.red = pixel_avg   
            pixel.green = pixel_avg
            pixel.blue = pixel_avg
    image.show()

if __name__ == '__main__':
    main()
