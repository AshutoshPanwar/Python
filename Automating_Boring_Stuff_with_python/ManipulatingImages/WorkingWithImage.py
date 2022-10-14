from PIL import Image

# Opne file
catIm = Image.open('dog.png')

# Know size of image
print('Image size in X, Y:')
print(catIm.size)

# Know file name
print("File name:")
print(catIm.filename)

# Know file format
print('File format:')
print(catIm.format)

# Save it to a new file.
print('Saving file as: copy.jpg')
print(catIm.save('copy.jpg'))