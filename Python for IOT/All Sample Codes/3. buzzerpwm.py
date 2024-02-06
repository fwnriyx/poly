import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep #used to create delays

GPIO.setmode(GPIO.BCM) #choose BCM mode
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT) #set GPIO 18 as output

PWM = GPIO.PWM(18,100) #set 100Hz PWM output at GPIO 18

while True: #loops the next 3 lines
    for i in range(0,101,20):
        PWM.start(i)
        sleep(0.5)
