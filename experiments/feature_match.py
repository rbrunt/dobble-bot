import cv2
import numpy as np
from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 10

def dowork():
    #img = cv2.imread('../img/three-cards.jpg', 0)
    img = cv2.imread('../img/test-2.jpg', 0)
    img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    img_orig = img.copy()

    #template = cv2.imread('../img/patterns/moon.jpg', 0)
    template = cv2.imread('../img/patterns/dinosaur.jpg', 0)
    #template = cv2.resize(template, (0, 0), fx=0.25, fy=0.25)
    
    scene = img.copy()
    symbol = template.copy()

    sift = cv2.xfeatures2d.SIFT_create()


    kp1, des1 = sift.detectAndCompute(symbol, None)
    kp2, des2 = sift.detectAndCompute(scene, None)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)
    
    matches = flann.knnMatch(des1, des2, k=2)

    good = []
    for m, n in matches:
        if m.distance < 0.7*n.distance:
            good.append(m)

    if len(good)>MIN_MATCH_COUNT:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        matchesMask = mask.ravel().tolist()

        h,w = symbol.shape
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts, M)

        scene = cv2.polylines(scene, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
    else:
        print "not enough good matches"
        matchesMask = None

    draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   matchesMask = matchesMask, # draw only inliers
                   flags = 2)

    img3 = cv2.drawMatches(symbol,kp1,scene,kp2,good,None,**draw_params)

    plt.imshow(img3, 'gray'),plt.show()

if __name__ == "__main__":
    dowork()
