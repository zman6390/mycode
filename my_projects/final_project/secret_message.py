from PIL import Image

# Convert string message to binary
def strToBin(msg):
    # use UTF-8 encoding to convert string to bytes
    # and then convert bytes to binary
    return ''.join(format(ord(i), '08b') for i in msg)

# Convert binary message to string
def binToStr(msg):
    # split binary message into chunks of 8 bits
    # convert each chunk to its corresponding ASCII character
    return ''.join(chr(int(msg[i:i+8], 2)) for i in range(0, len(msg), 8))

# Hide message in image
def hideMsgInImage(imgPath, msg):
    # Open the image file
    img = Image.open(imgPath)
    print(imgPath)

    # Convert the message to binary
    binMsg = strToBin(msg)
# Check if the message can fit in the image
    maxMsgLen = (img.size[0] * img.size[1] * 3) // 8
    if len(binMsg) > maxMsgLen:
        raise ValueError('Message too large to hide in image')

    # Create a list of all pixels in the image
    pixels = list(img.getdata())

    # Modify the least significant bit of each pixel to store the message
    bitIdx = 0
    for i in range(len(pixels)):
        pixel = list(pixels[i])
        for j in range(3):
            if bitIdx < len(binMsg):
                # Modify the least significant bit of the color channel
                pixel[j] = (pixel[j] & ~1) | int(binMsg[bitIdx])
                bitIdx += 1
        pixels[i] = tuple(pixel)

    # Create a new image with the modified pixels
    newImg = Image.new(img.mode, img.size)
    newImg.putdata(pixels)

    # Save the new image with the same filename as the original image
    newImg.save(imgPath)
  # Extract message from image
def extractMsgFromImage (imgPath):
    # Open the image file
    img = Image.open(imgPath)
    rgb_img = img.convert('RGB')
    rgb_img.save(imgPath)

    # Create a list of all pixels in the image
    pixels = list(img.getdata())

    # Extract the least significant bit of each color channel to reconstruct the message
    bitIdx = 0
    binMsg = ''
    for i in range(len(pixels)):
        for j in range(3):
            if bitIdx < 8:
                # Extract the least significant bit of the color channel
                binMsg += str(pixels[i][j] & 1)
                bitIdx += 1
            else:
                # Convert the binary message back to a string and return it
                return binToStr(binMsg)

    # Convert the binary message back to a string and return it
    return binToStr(binMsg)

# Example usage:
# Hide a message in an image
hideMsgInImage('image.png', 'Hello, world!')

# Extract the message from the image
msg = extractMsgFromImage('image.png')
print(msg)  # should print "Hello, world!"
