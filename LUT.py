import cv2 as cv
import numpy as np
def calculate_LUT(cdf_gi,cdf_gj) :
    lookup_table = np.zeros(256,1)
    g_j = 0 #LUT value
    for g_i in range (0,255):
        while (cdf_gj < cdf_gi) & (g_j < 255):
            g_j +=1
        lookup_table[g_i +1] = g_j
    return g_j


def matching_histogram(path = "/Users/lehuy/Desktop/01.jpeg"):
    img = cv.imread(path)
    print(img.shape)
    

    #cv.imshow('before', img)
    #cv.waitKey(0)
    #cv.destroyWindow()


def cdf_gi(img, g_i):
    count = len(img[img < g_i])
    sum = len(img) * len(img[0])
    p1 = count / sum;
    img[g_i+1] = p1
    return p1

def cdf_gj(img, g_j):
    count = len(img[img < g_j])
    sum = len(img) * len(img[0])
    p2 = count / sum;
    img[g_j + 1] = p2
    return p2

img = matching_histogram()
cv.imshow('after',img)
cv.waitKey()
cv.destroyWindow()
