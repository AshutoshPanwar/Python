from PIL import Image

# Open file
catIm = Image.open('dog.png')
# Creating a deep copy to play with
catCopyIm = catIm.copy()
# Getting cope image to pasted
faceIm = catIm.crop((335, 345, 565, 560))
# Getting size of cropped image
print('Size of croped image:')
print(faceIm.size)
# Pasting crop image to copyImage
catCopyIm.paste(faceIm, (0,0))
catCopyIm.paste(faceIm, (400, 500))
# Save file
print('Saving new image with name: pasted.png')
catCopyIm.save('pasted.png')