from PIL import Image, ImageFilter, ImageEnhance
import os

path = "./images"
pathOut = "./editedImages"

# Gets every image file in the images directory
for file_name in os.listdir(path):
    # Opens the image file
    image = Image.open(f"{path}/{file_name}")

    # Enhances and sharpens the image
    enhanced_image = image.filter(ImageFilter.EDGE_ENHANCE).filter(ImageFilter.SHARPEN)

    # Increases brightness by 5%
    factor = 1.05
    brightness_enhancer = ImageEnhance.Brightness(enhanced_image)
    enhanced_image = brightness_enhancer.enhance(factor)

    # Resizes the image to 500x500 while maintaining aspect ratio
    enhanced_image.thumbnail((500, 500))

    new_file_name = os.path.splitext(file_name)[0]

    enhanced_image.save(f"{pathOut}/edited_{new_file_name}.jpg")
