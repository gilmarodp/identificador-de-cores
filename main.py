import numpy as np
import imutils
import cv2

# definindo constantes de intervalos de cores...
LOWER = {
    'red': (166, 84, 141),
    'blue': (97, 100, 117),
    'yellow': (23, 59, 119)
}

UPPER = {
    'red': (186, 255, 255),
    'blue': (117, 255, 255),
    'yellow': (54, 255, 255)
}

# definindo cores dos contornos
OUTLINE_COLORS = {
    'red': (0, 0, 255),
    'blue': (255, 0, 0),
    'yellow': (0, 255, 217)
}

camera = cv2.VideoCapture(0)

while True:
    
    # read the video in real time
    (_, frame) = camera.read()
    
    # resize the frame
    frame = imutils.resize(frame, width=1000)
    
    # convert it to the HSV 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Construir uma mascara para a cor verde e outra pra a cor amarela
	# Uma serie de dilatacoes e erosoes para remover qualquer ruido
    mask_red = cv2.inRange(hsv, LOWER['red'], UPPER['red'])
    mask_red = cv2.erode(mask_red, None, iterations=2)
    mask_red = cv2.dilate(mask_red, None, iterations=2)
    
    mask_blue = cv2.inRange(hsv, LOWER['blue'], UPPER['blue'])
    mask_blue = cv2.erode(mask_blue, None, iterations=2)
    mask_blue = cv2.dilate(mask_blue, None, iterations=2)
    
    mask_yellow = cv2.inRange(hsv, LOWER['yellow'], UPPER['yellow'])
    mask_yellow = cv2.erode(mask_yellow, None, iterations=2)
    mask_yellow = cv2.dilate(mask_yellow, None, iterations=2)
    
    # Encontra os contornos das mascáras
    cont_red = cv2.findContours(mask_red.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center_red = None
    
    cont_blue = cv2.findContours(mask_blue.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center_blue = None
    
    cont_yellow = cv2.findContours(mask_yellow.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center_yellow = None
    
    if len(cont_red) > 0:
		# Encontrar o maior contorno da mascara, em seguida, usar-lo para calcular o circulo de fecho minima e
		# centroid
        c_red = max(cont_red, key=cv2.contourArea)
        rect_red = cv2.minAreaRect(c_red)
        box_red = cv2.boxPoints(rect_red)
        # print(box_yellow)
        box_red = np.int0(box_red)
        print(box_red[0][1])
        m_red = cv2.moments(c_red)
        center_red = (int(m_red["m10"] / m_red["m00"]), int(m_red["m01"] / m_red["m11"]))
        cv2.drawContours(frame, [box_red], 0, (0, 0, 255), 5)
        
        # mostrando nome logo abaixo do contorno
        underbox_position = (10, 50)
        cv2.putText(frame, 'Tem vermelho', underbox_position, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
        
    if len(cont_blue) > 0:
		# Encontrar o maior contorno da mascara, em seguida, usar-lo para calcular o circulo de fecho minima e
		# centroid
        # Encontrar o maior contorno da mascara, em seguida, usar-lo para calcular o circulo de fecho minima e
		# centroid
        c_blue = max(cont_blue, key=cv2.contourArea)
        rect_blue = cv2.minAreaRect(c_blue)
        box_blue = cv2.boxPoints(rect_blue)
        # print(box_yellow)
        box_blue = np.int0(box_blue)
        print(box_blue[0][1])
        m_blue = cv2.moments(c_blue)
        center_blue = (int(m_blue["m10"] / m_blue["m00"]), int(m_blue["m01"] / m_blue["m11"]))
        cv2.drawContours(frame, [box_blue], 0, (255, 0, 0), 5)
        
        # mostrando nome logo abaixo do contorno
        underbox_position = (10, 80)
        cv2.putText(frame, 'Tem azul', underbox_position, cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
        
    if len(cont_yellow) > 0:
		# Encontrar o maior contorno da mascara, em seguida, usar-lo para calcular o circulo de fecho minima e
		# centroid
        c_yellow = max(cont_yellow, key=cv2.contourArea)
        rect_yellow = cv2.minAreaRect(c_yellow)
        box_yellow = cv2.boxPoints(rect_yellow)
        # print(box_yellow)
        box_yellow = np.int0(box_yellow)
        print(box_yellow[0][1])
        m_yellow = cv2.moments(c_yellow)
        center_yellow = (int(m_yellow["m10"] / m_yellow["m00"]), int(m_yellow["m01"] / m_yellow["m11"]))
        cv2.drawContours(frame, [box_yellow], 0, (0, 255, 217), 5)
        
        # mostrando nome logo abaixo do contorno
        underbox_position = (10, 110)
        cv2.putText(frame, 'Tem amarelo', underbox_position, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 217), 3)

    # Mostrar o quadro na tela
    cv2.imshow("Identificador de cores", frame)
    key = cv2.waitKey(1) & 0xFF

	# Condicao de parada 'q', parar o loop
    if key == ord("q"):
        break
    