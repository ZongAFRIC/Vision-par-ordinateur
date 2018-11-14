# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:50:37 2018

@author: onezongoforall
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL.Image import*

"""lecture de l'image """
color = cv2.imread("/home/onezongoforall/Bureau/m.jpg",1)

cv2.imshow('original', color)

Lab = cv2.cvtColor(color, cv2.COLOR_BGR2Lab)

""" Construction de matrice nulle """
zeros = np.zeros(Lab.shape[:2], dtype="uint8")
#print(zeros)

"""enregister l'image"""
cv2.imwrite("/home/onezongoforall/Bureau/m.jpg", Lab)

"""lire l'image """
lab = cv2.imread("/home/onezongoforall/Bureau/m.jpg")

"""afficher l'image en espace lab"""
cv2.imshow('Lab', lab)

#-----Splitting the LAB image to different channels--------
l, a, b = cv2.split(lab)

splitLab = np.concatenate((l,a,b), axis=1)
cv2.imshow("split Lab", splitLab)
#cv2.imshow('l_channel', l)
#cv2.imshow('a_channel', a)
#cv2.imshow('b_channel', b)

"""Remplacement du paramètre L par la matrice nulle de même dimension"""
cv2.imshow("ab", cv2.merge([zeros, a, b]))
  
"""recuperation de la taille de la matrice nombre de ligne dans x et nombre de colonnes dans y"""  
def mystere(i):
    (largeur,hauteur)=i.size
    for y in range(hauteur):
        for x in range(largeur):
            pixel=Image.getpixel(i,(x,y))
            pixel=pixel/largeur*hauteur
            listdesProba[x][y]=pixel
            Image.putpixel(i,(x,y),inv)
i=open("/home/onezongoforall/Bureau/python/vo.png")
#Image.show(i)
#print(listdeProba)
#mystere.show(i)
#Image.show(i)       
       
        
        



img = cv2.imread("/home/onezongoforall/Bureau/m.png")
#plt.hist(img.ravel(),256,[0,256])
#plt.show()
Image.show(img)
mystere.show(img)

cv2.waitKey(0)
cv2.destroyAllWindows()



git remote add origin https://github.com/ZongAFRIC/inoussa1.git
