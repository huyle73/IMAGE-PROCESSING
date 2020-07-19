#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 11:18:49 2020

@author: lehuy
@supervisor : NguyenVanAnh
"""
import cv2
def increase_brightness(path = '/Users/lehuy/Desktop/01.jpeg') :
    img = cv2.imread(path)
    print(img.shape)
    cv2.imshow('before',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    value = 10
    for i in range(len(img)):
        for j in range(len(img[0])):
            for k in range(3):
                
                img[i,j,k] += value
                if(img[i,j,k] > 255):
                    img[i,j,k] = 255

def decrease_contrast(path = '/Users/lehuy/Desktop/01.jpeg') :
    img = cv2.imread(path)
    print(img.shape)
    cv2.imshow('before test',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    a = 1.6
    s = 128
    for i in range(len(img)):
        for j in range(len(img[0])):
            for k in range(3):
                img[i,j,k] = a*(img[i,j,k] -s) + s     
                if(img[i,j,k] <0) :
                    img[i,j,k] = 0
                elif(img[i,j,k] >255):
                     img[i,j,k] = 255
    
    #return imge
#print(img)
    
def hstogram_equalization(path = '/Users/lehuy/Desktop/01.jpeg') :
    img = cv2.imread(path)
    print(img.shape)
    
    
def gamma(path = '/Users/lehuy/Desktop/01.jpeg'):
    img = cv2.imread(path)
    cv2.imshow('before test',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(img.shape)
    # if gamma >1.0 : incrase; 
    # if gamme <1.0 : decrease
    gamma = 4
    for i in range (len(img)):
        for j in range(len(img[0])):
           img[i,j] = 255 * (img[i,j]/255) ** (1/gamma)
    
    #return img


def contrast_stretch(path =  '/Users/lehuy/Desktop/01.jpeg'):
    img = cv2.imread(path)
    cv2.imshow('before test',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(img.shape)
    for i in range (len(img)):
        for j in range (len(img[0])):
           m_i = min(img[i,j])
           M_i = max(img[i,j])
           #constrast_stretch value if u want to stretch.
           m_j = 124
           M_j = 88
           #M_j = max(img1[i,j])
           img[i,j] = (M_j - m_j) * ((img[i,j]- m_i)/(M_i-m_i)) + m_j
           
    #return img

def Luminance_histogram(path = '/Users/lehuy/Desktop/01.jpeg') :
    img = cv2.imread(path)
    cv2.imshow('before test',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(img.shape)
    for i in range(len(img)):
        for j in range (len(img[0])):
            for k in range(3) :
                img[i,j] = 0.299* img[i,j,0] + 0.587* img[i,j,1] + 0.114 * img[i,j,2]
                
    return img




def Probability_Density(pat = '/Users/lehuy/Desktop/01.jpeg') :
    img = cv2.imread(path)
    cv2.imshow('before test',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(img.shape)
           
            
    
   

#print(img)
img = contrast_stretch()
cv2.imshow('after',img)
cv2.waitKey(0)
cv2.destroyAllWindows()





