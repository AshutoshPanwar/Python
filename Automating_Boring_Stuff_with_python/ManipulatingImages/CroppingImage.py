from PIL import Image

# Open file
catIm = Image.open('dog.png')
# Crop Image
croppedIm = catIm.crop((335, 343, 565, 560))
# Save the crop image as copy
croppedIm.save('cropped.png')