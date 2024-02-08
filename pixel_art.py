import argparse
from pathlib import Path
from skimage import io
from PIL import Image
from pyxelate import Pyx

def resize_image(image_path, max_width=1920):
    with Image.open(image_path) as im:
        if im.width > max_width:
            factor = max_width / im.width
            im_resized = im.resize((int(im.width * factor), int(im.height * factor)))
            im_resized.save(image_path, quality=100, subsampling=0)

def pixelate_image(image_path, downsample_by=6, palette=16):
    image = io.imread(image_path)
    
    # Pyxelate for pixelation
    pyx = Pyx(factor=downsample_by, upscale=downsample_by, palette=palette)
    pyx.fit(image)
    new_image = pyx.transform(image)

    # Save the result
    name = Path(image_path).stem
    io.imsave(f"{name}_pixel.png", new_image)

def main():
    parser = argparse.ArgumentParser(description="ドット絵に変換")
    parser.add_argument("filename", help="変換してほしいもの")
    args = parser.parse_args()

    # Resize the image if it exceeds the maximum width
    resize_image(args.filename)

    # Pixelate the image
    pixelate_image(args.filename)

if __name__ == "__main__":
    main()
