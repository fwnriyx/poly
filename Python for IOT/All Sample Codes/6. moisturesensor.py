import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep

GPIO.setmode(GPIO.BCM) #choose BCM mode
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.IN) #set GPIO 4 as input
while (True):
    if GPIO.input(4): #if read a high at GPIO 4, moisture present
        print('detected HIGH i.e. moisture')
    else: #otherwise (i.e. read a low) at GPIO 4, no moisture
        print('detected LOW i.e. no moisture')
    sleep(0.5) # to limit print() frequency
