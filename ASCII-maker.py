import argparse
from PIL import Image

# Define the characters to use for the ASCII art
CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

# Define the dimensions of the terminal window
TERMINAL_WIDTH = 80
TERMINAL_HEIGHT = 40

# Define the scale factor for the image
SCALE_FACTOR = 0.1

def resizeImage(image):
    """Resize the image to fit within the terminal window"""
    imageWidth, imageHeight = image.size
    if imageWidth > TERMINAL_WIDTH * SCALE_FACTOR or imageHeight > TERMINAL_HEIGHT * SCALE_FACTOR:
        scaleFactor = min(TERMINAL_WIDTH * SCALE_FACTOR / imageWidth, TERMINAL_HEIGHT * SCALE_FACTOR / imageHeight)
        newWidth = int(imageWidth * scaleFactor)
        newHeight = int(imageHeight * scaleFactor)
        return image.resize((newWidth, newHeight))
    else:
        return image

def imageToAscii(image):
    """Convert the image to ASCII art"""
    image = resizeImage(image)
    pixels = image.convert('L').getdata()
    asciiChars = [CHARS[pixel // 25] for pixel in pixels]
    return ''.join(asciiChars)

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Convert an image to ASCII art.')
    parser.add_argument('image', type=str, help='the image file to convert')
    args = parser.parse_args()

    # Load the image file and convert it to ASCII art
    image = Image.open(args.image)
    asciiArt = imageToAscii(image)

    # Print the ASCII art to the console
    print(asciiArt)
