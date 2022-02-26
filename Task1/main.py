import cv2
import numpy as np
import os
from PIL import Image

"""Defining all the outputs to a Seperate folder using the os module"""
def create(fadd):
    ia = []
    for file in os.listdir(fadd):
        ipath = os.path.join(fadd, file)
        image = cv2.imread(ipath, cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(image, (512, 512), interpolation=cv2.INTER_AREA)
        cv2.imwrite(f'C:/Users/Aravind/Desktop/ara/Output/gray_{file}',image)
        print(len(image))
        print(image.dtype)
        #ia.append(img)
        # cv2.imshow('image', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    return ia


fadd = r"C:/Users/Aravind/Desktop/ara/dataset"
res = create(fadd)
print(res)
