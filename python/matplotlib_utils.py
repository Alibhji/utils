# Ali Babolhavaeji Jan/2022
# this file contains snippet scripts for Matplotlib

import matplotlib.pyplot as plt
import numpy as np
import cv2

# Display a list of images in a row
# It takes ( [img1,img2, ...] , ['title1' , 'title2',...])
def display(display_list , title):
    plt.figure(figsize=(15, 15))
    for i in range(len(display_list)):
        plt.subplot(1, len(display_list), i+1)
        plt.title(title[i])
        plt.imshow(display_list[i])
        plt.axis('off')
    plt.show()


def display_in_different_rows( img_pathes , each_row = 4 , tagnet = None):
    def read_image(path):
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img

    nsegs = len(img_pathes) // each_row

    display_list = [read_image(img) for img in img_pathes]
    splited_list = np.array_split(display_list, nsegs)
    nrows = len(splited_list)
    ncols = len(splited_list[0])
    count = 0
    plt.figure(figsize=(15 , 3*nrows))
    for r ,row in enumerate(splited_list):
        for i in range(len(row)):
            count+=1
            plt.subplot(nrows, ncols ,count )
            title = f"{img_pathes[count-1].split('/')[-1]}"

            if not tagnet is None:
                title += f" {tagnet[count-1]}"
            plt.title(title)

            plt.imshow(row[i])
            plt.axis('off')
    plt.subplots_adjust(wspace=0, hspace=0.12)
    plt.show()


