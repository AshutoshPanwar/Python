from PIL import Image

# Opne image
catIm = Image.open('dog.png')
width, height = catIm.size
# Resize it to half of it's size
quartersizeIm = catIm.resize((int(width/2), int(height/2)))
quartersizeIm.save('quartersize.png')
# Again resize
svelteIm = catIm.resize((width, height + 500))
svelteIm.save('svelte.png')