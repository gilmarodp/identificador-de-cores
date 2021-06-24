import cv2 as cv

def device_list():
    device_list= []
    index = 0
    
    while index < 5:
        capture = cv.VideoCapture(index)
        if capture.isOpened():
            device_list.append(index)
            
        index += 1
        
    return device_list


def show_devices_and_get_answer():
    answer = None
    devices = device_list()
    
    if devices is None:
        print('Você não possui câmeras diponíveis...')
        quit
        
    print(f'Você possui {len(devices)} dispositivos disponíveis.\n')
    for device in devices:
        print(f'[ {device} ] -> Câmera {device}')
        

    while answer is None or not answer in devices:
        answer = int(input('\n>: '))
    
    return answer
