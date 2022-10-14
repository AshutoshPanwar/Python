from PIL import Image

# Opne file
catIm = Image.open('dog.png')

# Rotating image with rotate and saving it to a new file
# rotate(ange*)
catIm.rotate(90).save('R90.png')
catIm.rotate(180).save('R180.png')
catIm.rotate(270).save('R270.png')