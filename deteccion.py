#Aca hacer la deteccion de alguna imagen
import numpy as np
from cv2 import cv2
import matplotlib as plt

img = cv2.imread("fotos/cuadrado.png")

img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Filtrar con un Blur Gaussiano
kernel = (11, 11)
img_gaus = cv2.GaussianBlur(img_gray, kernel, 0)

# Aplicar filtro Canny para detección de bordes
img_canny = cv2.Canny(img_gaus, 10, 100)

# Suavizar la imagen con erode y dilate
img_filtered = cv2.dilate(img_canny, (2,2))
img_filtered = cv2.erode(img_filtered, (2,2))

#cv2.imshow("prueba", img_canny)

# Encontrar contornos
contours, hierarchy = cv2.findContours(img_filtered, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


# Filtrar los contornos obtenidos para quedarse sólo con aquellos cuya área sea suficientemente grande (>1000px)
contornos_buenos = []
for c in contours:
    if cv2.contourArea(c) >= 1000:
        contornos_buenos.append(c)

contours = contornos_buenos

cv2.drawContours(img, contours, -1, (0,0,255), 6)
for c in contours:
    #Sacamos el centro de la imagen
    M = cv2.moments(c)
    if M['m00'] != 0:
        #cx y cy es el centro y usamos esto pa mover al roboc?
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.circle(img, (cx, cy),0,  (0,255,0), 5)

#mostramos la imagen
cv2.imshow("imagen", img)
cv2.waitKey(0)
cv2.destroyAllWindows()