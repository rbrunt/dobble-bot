import numpy as np
import cv2

if __name__ == "__main__":

    img = cv2.imread("movember.jpg", 0)

    cv2.imshow('movember', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

