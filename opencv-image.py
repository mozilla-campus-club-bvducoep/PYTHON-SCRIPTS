//Install numpy and opencv using pip

import numpy as np
import cv2

img = cv2.imread('image_path_here', 1)   #importing image

cv2.imshow('image',img)  #Showing images 

k = cv2.waitKey(0) 

##### Press any Key TO close #########
