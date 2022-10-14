from PIL import Image

# Creating image of color purple of size(100*200)
img = Image.new('RGBA', (100, 200), 'purple')
print('Saving file with name: purpleImage.png')
img.save('purpleImage.png')

# Creating Transpared image
img1 = Image.new('RGBA', (100, 200))
print('Saving file with name: Transpared.png')
img1.save('Transpared.png')