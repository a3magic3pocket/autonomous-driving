from pywinauto import findwindows, application, keyboard
import sys
import pytesseract
import os
import PIL
import cv2
import numpy as np

if __name__ == "__main__":
    pytesseract.pytesseract.tesseract_cmd = r'E:\\Program_Files\\Tesseract-OCR\\tesseract'

    img_dir_path = 'img'
    file_paths = os.listdir(img_dir_path)
    
    for i, file_path in enumerate(file_paths):
        img_path = f"{img_dir_path}/{file_path}"
        
        img = PIL.Image.open(img_path)
        img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
        ret, img = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY)
        # img = cv.threshold(img,127,255,cv.THRESH_BINARY)
        
        # PIL.Image.fromarray(img).show()
        # sys.exit(1)
        a = pytesseract.image_to_string(img,  config='--psm 1 --oem 3 digits')
        
        PIL.Image.fromarray(img).save(f"refined_img/{i}_{a.strip()}.png")
        print(f"{a=}")
