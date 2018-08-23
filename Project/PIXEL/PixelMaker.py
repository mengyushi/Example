import matplotlib
import numpy as np
import matplotlib.pyplot as plt

import skimage
from skimage import data
import math

def pixel_maker(filename,resolution):
    
    im = plt.imread(filename)
    X = im.shape[0]
    Y = im.shape[1]
    
    if resolution>X or resolution>Y:
        print("Resolution required larger than origin.")
        return 
    

    piX = resolution
    piY = math.floor((piX/X)*Y)
    
    sec = math.floor(X/piX)
    
    small = np.zeros((piX,piY,3))
    
    for x in range(piX):
        for y in range(piY):
            small[x][y] = im[x*sec][y*sec]/256
    plt.axis('off')
    plt.imshow(small)
    plt.savefig("PIXEL_"+filename)
    
filename = str(input("Give me the name of original pic?    "))
resolution = int(input("What resolution would you like?    "))
print("Processing...")

pixel_maker(filename,resolution)

_ = input("Finished!")