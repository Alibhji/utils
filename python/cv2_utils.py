# Ali Babolhavaeji Jan/2022
# this file contains snippet scripts for open-cv

# Overlay two images by open-cv and draw them:
import cv2
import numpy as np

def overlay_two_images(bg_image , bin_mask ):
    # bg_image has type of uint8

    # add a new dimension to the 2d mask image
    bin_mask = bin_mask[:, :, np.newaxis]
    # mask  quantization
    bin_mask = bin_mask * 255
    # make it a 3 channel image (RGB) and convert it to the uint8
    bin_mask = np.concatenate((bin_mask, np.tile(np.zeros_like(bin_mask), [1, 1, 2])), axis=-1).astype(np.uint8)
    #change the order of RGB layers to see different color on the overlaid image
    bin_mask = bin_mask[:, :, [1, 2, 0]]
    # add two images
    added_image = cv2.addWeighted(bg_image, 0.2, bin_mask, 1, 0.9)
    return added_image



