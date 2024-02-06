import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep

GPIO.setmode(GPIO.BCM) #choose BCM mode
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.IN) #set GPIO 22 as input

while(True): #loop
    if GPIO.input(22): #if read a high at GPIO 22
        print("detected HIGH i.e. slider at 3.3V side")
    else: #otherwise (i.e. read a low) at GPIO 22
        print("detected LOW i.e. slider at GND side")
    sleep(0.5) # to limit print() frequency
