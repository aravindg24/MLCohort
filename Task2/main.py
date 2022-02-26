import cv2
import pandas as pd
import os

"""For Labelling Single Image we can write like this..."""
# df = pd.read_csv("C:/Users/Aravind/Desktop/ara1/data_labels.csv")
# ipath = "C:/Users/Aravind/Desktop/ara1/cat/cats_000.jpg"
# count = 1
# label = df['label'][count]
#
# image = cv2.imread(ipath)
# rectangle=cv2.rectangle(image, (int(df['xmin'][count]), int(df['ymax'][count])), (int(df['xmax'][count]), int(df['ymin'][count])),(255, 0, 0), 2)
# text =cv2.putText(rectangle, label , (500,500), cv2.FONT_HERSHEY_SIMPLEX,4,(0, 0, 0), 4)
# cv2.imshow('image', text)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""For labelling Multiple Images ina Folder we write Like This"""

df = pd.read_csv("C:/Users/Aravind/Desktop/ara1/data_labels.csv")
path = "C:/Users/Aravind/Desktop/ara1/cat"

def create(path):
    count = 1

    for file in os.listdir(path):
        ip = os.path.join(path, file)
        image = cv2.imread(ip)
        rectangle = cv2.rectangle(image, (int(df['xmin'][count]), int(df['ymax'][count])),(int(df['xmax'][count]), int(df['ymin'][count])), (255, 0, 0), 2)
        org = (50,50)
        text =cv2.putText(rectangle, df['label'][count] ,org, cv2.FONT_HERSHEY_SIMPLEX,1,(255, 0, 0), 4,cv2.LINE_AA)
        count += 1
        cv2.imwrite(f'C:/Users/Aravind/Desktop/ara1/Output/label_{file}', text)
        # cv2.imshow('image', text)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

create(path)


