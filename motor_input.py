import RPi.GPIO as GPIO 
import time 

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
speed = 5
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
        

while True:
    command = input("=>").replace(" ","")
    if "q" == command:
        break
    if "l" == command:
        rotate_left()
        clearmotor()
    if "r" == command:
        rotate_right()
        clearmotor()
        
    if "s" == command:
        speed = get_speed()








GPIO.cleanup()