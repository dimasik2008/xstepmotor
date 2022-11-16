import RPi.GPIO as GPIO 
import time 
import socket
import threading
import logging
logging.basicConfig(level=logging.WARN)
GPIO.setmode(GPIO.BOARD)
Controlpins = [7,11,13,15]

for pin in Controlpins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)
    
right = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1],
]
left = [
    [1,0,0,1],
    [0,0,0,1],
    [0,0,1,1],
    [0,0,1,0],
    [0,1,1,0],
    [0,1,0,0],
    [1,1,0,0],
    [1,0,0,0],
    
]

# for i in range(1):
#     for _,halfstep in enumerate(steps):
#         for pi,pin in enumerate(Controlpins):
#             GPIO.output(pin,halfstep[pi])
#         time.sleep(0.001)

def get_speed():
    speed = input("speed=>")
    return int(speed)

def rotate_left():
    for i in range(speed):
        for _,halfstep in enumerate(right):
            for pi,pin in enumerate(Controlpins):
                GPIO.output(pin,halfstep[pi])
            time.sleep(0.001)
            
def rotate_right():
    for i in range(speed):
        for _,halfstep in enumerate(left):
            for pi,pin in enumerate(Controlpins):
                GPIO.output(pin,halfstep[pi])
            time.sleep(0.001)

def clearmotor():
    for pin in Controlpins:
        GPIO.output(pin,0)
        
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
print('connected:', addr)

dim = "n"
speed = 1
def control():
    global dim
    while 1:
        if "r" in dim:
            rotate_right()
            clearmotor()
        elif "l" in dim:
            rotate_left()
            clearmotor()
        else:
            clearmotor()
threading.Thread(target=control).start()
while True:
    dim = conn.recv(1024).decode()
    logging.info(dim)
