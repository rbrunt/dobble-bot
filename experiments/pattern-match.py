import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../img/three-cards.jpg', 0)
img = cv2.resize(img, (0,0), fx=0.25, fy=0.25)
img2 = img.copy()
template = cv2.imread('../img/patterns/moon.jpg', 0)
template = cv2.resize(template, (0,0), fx=0.25, fy=0.25)
w, h = template.shape[::-1]

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

img = img2.copy()
method = cv2.TM_CCOEFF

res = cv2.matchTemplate(img, template, method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left= max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(img, top_left, bottom_right, 255, 2)

cv2.imshow('detected circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

