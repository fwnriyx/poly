import RPi.GPIO as GPIO
import dht11
import time
import datetime

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

instance = dht11.DHT11(pin=21) #read data using pin 21

try:
    while True: #keep reading, unless keyboard is pressed
        result = instance.read()
        if result.is_valid(): #print datetime & sensor values
            print("Last valid input: " +     
                str(datetime.datetime.now()))
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
        time.sleep(0.5) #short delay between reads

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()