from PIL import ImageColor

# Get RGBA color code of a color
# Getcolor take two arguments (color, ToType) as string
print("RGBA value of 'RED' Color:")
print(ImageColor.getcolor('red', 'RGBA'))
print("RGBA value of 'BLACK' Color:")
print(ImageColor.getcolor('black', 'RGBA'))
print("RGBA value of 'Chocolate' Color:")
print(ImageColor.getcolor('chocolate', 'RGBA'))