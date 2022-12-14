from PIL import Image
from PIL.ExifTags import TAGS
import os
print(TAGS)
image_path = "./images/"
for file in os.listdir(image_path):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".JPG"):
        img = Image.open(image_path + file)
        exif_data = img.getexif()
        info_dict = {
            "Filename": img.filename,
            "Size": img.size,
            "Height": img.height,
            "Width": img.width,
            "Format": img.format,
            "Mode": img.mode,
            "is Animated": getattr(img, "is_animated", False),
            "Frames in Image": getattr(img, "n_frames", 1)
        }
    else:
        print("Not a jpg")
        continue

for label,value in info_dict.items():
    print(f"{label:25}: {value} SEX1")
