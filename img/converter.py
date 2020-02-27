from PIL import Image
import glob


for file in glob.glob("*.png"):
    img = Image.open(file)
    rgb_im = img.convert('RGB')
    rgb_im.save(file.replace("png", "bmp"), quality=95)
