
def isLandscape (height, width):
    if width > height:
        return "landscape"
    else:
        return "portrait"
    

image_height = float(input("What is the image height? "))
image_width = float(input("What is the image width? "))

image_type = isLandscape(image_height, image_width)

print(f"It is a {image_type} image.")
