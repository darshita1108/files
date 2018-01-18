from PIL import Image

img = Image.open("france3.jpg")
print(img.size)
print(img.format)

img.show()
