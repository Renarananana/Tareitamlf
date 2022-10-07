import time
import deteccion
from client import RobotClient
from inverseKinematics import position_to_dof
import numpy as np
import cv2
from move_the_robot import move_robot_to_xyz

# Conectarse al robot

r = RobotClient(address="127.0.0.1")  # Recuerda usar una dirección válida
r.connect()
r.home()  # Revisa el archivo client.py para que veas qué hace esta función

df = deteccion.Detectar_figura()



img = cv2.imread("fotos/cuadrado.png")
x, y = df.encontrar_centro(img)
if (x == 0 and y == 0):
    exit()

#TRANSFORMACION
const=1.61

centro_img =  (160, 120)

pos_fig_pix = (x,y) - centro_img
pos_fig_mm = pos_fig_pix*const
x,y = pos_fig_mm
pos_fig_mm_al_r = np.array([-y,-x])
pos_fig_mm_r = pos_fig_mm_al_r+np.array([170,0]) #posicion de la figura en el sistema de referencia del robot (mm)
print(pos_fig_mm_r)
move_robot_to_xyz(r,pos_fig_mm_r[0], pos_fig_mm_r[y], 20)





