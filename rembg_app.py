from rembg import remove
import cv2

def main():
    input_path = 'image.jpg'
    output_path = 'rembg_image.png'

    input = cv2.imread(input_path)
    output = remove(input)
    cv2.imwrite(output_path, output)

if __name__ == "__main__":
    main()