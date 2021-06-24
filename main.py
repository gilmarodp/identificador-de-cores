import numpy as np
import cv2 as cv
import imutils

from src.colors import *

camera = cv.VideoCapture(0)

while True:
    
    # read the video in real time
    (_, frame) = camera.read()
    
    # resize the frame
    frame = imutils.resize(frame, width=1000)
    
    # convert it to the HSV 
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Construir uma mascara para a cor verde e outra pra a cor amarela
	# Uma serie de dilatacoes e erosoes para remover qualquer ruido
    mask_red = cv.inRange(hsv, LOWER['red'], UPPER['red'])
    mask_red = cv.erode(mask_red, None, iterations=2)
    mask_red = cv.dilate(mask_red, None, iterations=2)
    
    mask_blue = cv.inRange(hsv, LOWER['blue'], UPPER['blue'])
    mask_blue = cv.erode(mask_blue, None, iterations=2)
    mask_blue = cv.dilate(mask_blue, None, iterations=2)
    
    mask_yellow = cv.inRange(hsv, LOWER['yellow'], UPPER['yellow'])
    mask_yellow = cv.erode(mask_yellow, None, iterations=2)
    mask_yellow = cv.dilate(mask_yellow, None, iterations=2)
    
    # Encontra os contornos das mascáras
    cont_red = cv.findContours(mask_red.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]
    center_red = None
    
    cont_blue = cv.findContours(mask_blue.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]
    center_blue = None
    
    cont_yellow = cv.findContours(mask_yellow.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]
    center_yellow = None
    
    if len(cont_red) > 0:
		# Encontrar o maior contorno da mascara, em seguida, usar-lo para calcular o circulo de fecho minima e
		# centroid
        c_red = max(cont_red, key=cv.contourArea)
        rect_red = cv.minAreaRect(c_red)
        box_red = cv.boxPoints(rect_red)
        # print(box_yellow)
        box_red = np.int0(box_red)
        print(box_red[0][1])
        m_red = cv.moments(c_red)
        center_red = (int(m_red["m10"] / m_red["m00"]), int(m_red["m01"] / m_red["m11"]))
        cv.drawContours(frame, [box_red], 0, (0, 0, 255), 5)
        
        # mostrando nome logo abaixo do contorno
        underbox_position = (10, 50)
        cv.putText(frame, 'Tem vermelho', underbox_position, cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
        
    if len(cont_blue) > 0:
		# Encontrar o maior contorno da mascara, em seguida, usar-lo para calcular o circulo de fecho minima e
		# centroid
        # Encontrar o maior contorno da mascara, em seguida, usar-lo para calcular o circulo de fecho minima e
		# centroid
        c_blue = max(cont_blue, key=cv.contourArea)
        rect_blue = cv.minAreaRect(c_blue)
        box_blue = cv.boxPoints(rect_blue)
        # print(box_yellow)
        box_blue = np.int0(box_blue)
        print(box_blue[0][1])
        m_blue = cv.moments(c_blue)
        center_blue = (int(m_blue["m10"] / m_blue["m00"]), int(m_blue["m01"] / m_blue["m11"]))
        cv.drawContours(frame, [box_blue], 0, (255, 0, 0), 5)
        
        # mostrando nome logo abaixo do contorno
        underbox_position = (10, 80)
        cv.putText(frame, 'Tem azul', underbox_position, cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
        
    if len(cont_yellow) > 0:
		# Encontrar o maior contorno da mascara, em seguida, usar-lo para calcular o circulo de fecho minima e
		# centroid
        c_yellow = max(cont_yellow, key=cv.contourArea)
        rect_yellow = cv.minAreaRect(c_yellow)
        box_yellow = cv.boxPoints(rect_yellow)
        # print(box_yellow)
        box_yellow = np.int0(box_yellow)
        print(box_yellow[0][1])
        m_yellow = cv.moments(c_yellow)
        center_yellow = (int(m_yellow["m10"] / m_yellow["m00"]), int(m_yellow["m01"] / m_yellow["m11"]))
        cv.drawContours(frame, [box_yellow], 0, (0, 255, 217), 5)
        
        # mostrando nome logo abaixo do contorno
        underbox_position = (10, 110)
        cv.putText(frame, 'Tem amarelo', underbox_position, cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 217), 3)

    # Mostrar o quadro na tela
    cv.imshow("Identificador de cores", frame)
    key = cv.waitKey(1) & 0xFF

	# Condicao de parada 'q', parar o loop
    if key == ord("q"):
        break
    