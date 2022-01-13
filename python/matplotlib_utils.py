# Ali Babolhavaeji Jan/2022
# this file contains snippet scripts for Matplotlib

import matplotlib.pyplot as plt

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