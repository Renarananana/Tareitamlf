#Aca hacer la deteccion de alguna imagen
import numpy as np
from cv2 import cv2
import matplotlib as plt

img = cv2.imread("fotos/circulo.png")

img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Filtrar con un Blur Gaussiano
kernel = (7, 7)
img_gaus = cv2.GaussianBlur(img_gray, kernel, 0)

# Aplicar filtro Canny para detección de bordes
img_canny = cv2.Canny(img_gaus, 10, 100)

# Suavizar la imagen con erode y dilate
img_filtered = cv2.dilate(img_canny, (2,2))
img_filtered = cv2.erode(img_filtered, (2,2))

# Encontrar contornos
contours, hierarchy = cv2.findContours(img_filtered, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


# Filtrar los contornos obtenidos para quedarse sólo con aquellos cuya área sea suficientemente grande (>10.000px)
contornos_buenos = []
for c in contours:
    if cv2.contourArea(c) >= 10000:
        contornos_buenos.append(c)

contours = contornos_buenos

for c in contours:

    # Calcular la cantidad de lados de la forma
    """ En esta sección se recomienda consultar el sitio https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/ """
    perimetro = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * perimetro, True)
    shape_size = len(approx)
    # Dibujar bounding box del contorno y agregar texto que lo describe
    x, y, w, h = cv2.boundingRect(approx)
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)


cv2.imshow("imagen", img)
cv2.waitKey(0)
cv2.destroyAllWindows()