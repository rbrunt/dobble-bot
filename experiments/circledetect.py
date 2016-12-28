import numpy as np
import cv2

if __name__ == "__main__":

    img = cv2.imread("../img/three-cards.jpg", 0)
    img = cv2.resize(img, (0,0), fx=0.25, fy=0.25)
    #img = cv2.medianBlur(img, 25)

    ret, img  =cv2.threshold(img, 127,255,cv2.THRESH_TOZERO)

    #img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

    img = cv2.medianBlur(img, 25)

    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    
    print "finding circles..."

    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

    print "finished finding circles"
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        #draw outer circle:
        cv2.circle(cimg, (i[0], i[1]), i[2], (0,255,0),2)
        #draw centre:
        cv2.circle(cimg, (i[0],i[1]), 2, (0,255,255),3)

    cv2.imshow('detected circles', cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

