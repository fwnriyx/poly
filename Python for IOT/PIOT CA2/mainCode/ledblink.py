import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep #used to create delays

GPIO.setmode(GPIO.BCM) #choose BCM mode
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.OUT) #set GPIO 24 as output

while True: #loops the next 4 lines
    GPIO.output(24,1) #output logic high/'1'
    sleep(1) #delay 1 second
    GPIO.output(24,0) #output logic low/'0'
    sleep(1) #delay 1 second
