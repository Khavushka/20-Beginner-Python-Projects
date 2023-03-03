# Image resizer using Python
# install pillow if you havent
# import pillow
# open up the image we want to resize using python
# specify the size we wanna change it to
# save the new resized image

from PIL import Image

image = Image.open('\img\sunrise.jpg')

print(f'Current size: {image.size}')

resized_image = image.resize((500, 500))

resized_image.save('new_image.jpg')