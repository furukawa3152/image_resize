import glob
from PIL import Image
files = glob.glob("img_data/*.jpg")
for file in files:
    filepass = file
    filename = file.split("\\")[1]
    try:
        img = Image.open(filepass)
        img_resize = img.resize((img.width // 3, img.height // 3))
        img_resize.save(f"resized_data/{filename}")
    except OSError:
        pass