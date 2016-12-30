import numpy as np
import cv2
import copy

class Circle(object):
    def __init__(self, centre, radius):
        self.x = centre[0]
        self.y = centre[1]
        self.centre = (self.x, self.y)
        self.radius = radius

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(tuple(self.x, self.y, self.radius))

    def __str__(self):
        return "Centre: {0}, {1}. Radius: {2}".format(self.x, self.y, self.radius)

    def __unicode__(self):
        return "Centre: {0}, {1}. Radius: {2}".format(self.x, self.y, self.radius)


def circle_is_inside_circle(littleCircle, bigCircle):
    #minX = bigCircle.x - bigCircle.radius
    #maxX = bigCircle.x + bigCircle.radius
    #minY = bigCirlce.y - bigCircle.radius
    #maxY = bigCircle.y + bigCircle.radius

    if (abs(bigCircle.x - littleCircle.x) < bigCircle.radius) and (abs(bigCircle.y - littleCircle.y) < bigCircle.radius):
        return True
    else:
        return False

def find_largest_non_overlapping_circles(circles_output):

    circles = [Circle((i[0], i[1]), i[2]) for i in circles_output[0,:]]
    circles.sort(key = lambda c: c.radius, reverse=True)

    circles_to_remove_from = list(circles)
    circles_to_remove = set()


    for i in xrange(len(circles)):
        bigCircle = circles[i]
        for j in xrange(len(circles)):
            if i < j:
                littleCircle = circles[j]
                if circle_is_inside_circle(littleCircle, bigCircle):
                    circles_to_remove.add(j)
                    if littleCircle in circles_to_remove_from:
                        circles_to_remove_from.remove(littleCircle)

    return circles_to_remove_from


if __name__ == "__main__":

    img = cv2.imread("../img/three-cards.jpg", 0)
    img = cv2.resize(img, (0,0), fx=0.25, fy=0.25)

    original_image = img.copy()
    #img = cv2.medianBlur(img, 25)

    ret, img  =cv2.threshold(img, 127,255,cv2.THRESH_TOZERO)

    #img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

    img = cv2.medianBlur(img, 25)

    cimg = cv2.cvtColor(original_image,cv2.COLOR_GRAY2BGR)
    
    print "finding circles..."

    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)


    sorted_circles = find_largest_non_overlapping_circles(circles)

    print "finished finding circles"
    circles = np.uint16(np.around(circles))
    for i in sorted_circles:
        #draw outer circle:
        cv2.circle(cimg, (i.x, i.y), i.radius, (0,255,0),2)
        #draw centre:
        cv2.circle(cimg, (i.x, i.y), 2, (0,255,255),3)

    cv2.imshow('detected circles', cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

