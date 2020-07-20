#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 20:22:49 2020

@author: lehuy
"""
import cv2
import numpy as np
#Lec03_Pointprocessing
def histogram_equalization (img):
    try:  
        a = np.ones(256) * -1
        m_j = 32
        M_j = 200
    
        m_i = np.min(img)
        M_i = np.max(img)
        img1 = img
        
        p_mi, a = cdf(img,m_i+1, a)
        p_Mi, a = cdf(img, M_i +1, a)
        
        print(p_mi, p_Mi)
        
        for i in range(len(img)):
            for j in range(len(img[0])):
                g = img[i,j] + 1
                
                p, a = cdf(img,g, a)
                img1[i, j] = (M_j - m_j) * (p - p_mi) / (p_Mi - p_mi) + m_j

        print('done')
    except:
        print(p)
    return img1

def cdf(img, g, a):
    if(a[g-1] == -1):
        count = len(img[img < g])
        sum_ = len(img) * len(img[0])
        p = count /sum_
        a[g-1] = p
    return a[g-1], a
    
    
  

path = "/Users/lehuy/Desktop/02.jpg"
img = np.asarray(cv2.imread(path))
print(img.shape)
img_c1 = img[:,:,0]
img_c2 = img[:,:,1]
img_c3 = img[:,:,2]

j_1 = histogram_equalization(img_c1)
j_2 = histogram_equalization(img_c2)
j_3 = histogram_equalization(img_c3)

j_com = img
for i in range(len(img)):
    for j in range(len(img[0])):
        for k in range (3) :
            if(k == 0):
                j_com[i, j, k] = j_1[i, j]
            if(k == 1):
                j_com[i,j,k] = j_2[i,j]
            else:
                j_com[i,j,k] = j_3[i,j]

cv2.imshow("after",j_com/255.0)
cv2.waitKey(0)
cv2.destroyAllWindows()


    
    
