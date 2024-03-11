# import RPi.GPIO as GPIO
# import RPi.GPIO as GPIO
# import I2C_LCD_driver
from time import sleep
# from mfrc522 import SimpleMFRC522
import os
import requests
import json
from PIL import Image
from io import BytesIO
# from mainCode.adxl345 import ADXL345
import random
# import dht11
import time    
# import telegram

# heart_rate = [52,50,51,53,55,57,58]

token = "6236591816:AAEAP8PT7j7PE-bCsrHkz4QtVqQtZOquK9Y"
url = f"https://api.telegram.org/bot{token}/getUpdates"
chat_id = "6236591816"


# Constants for keypad and RFID modes
RFID_MODE = 1
FITNESS_MODE = 2
# accelerometer = ADXL345(i2c_port=1, address=0x53)

current_dir = os.getcwd()

# Initialize variables
mode = ''
buzzer = 18
counter = 0
num = ''
auth = []

#GPIO
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)

# #servo motor
# GPIO.setmode(GPIO.BCM) #choose BCM mode
# GPIO.setwarnings(False)
# GPIO.setup(26,GPIO.OUT) #set GPIO 26 as output
# GPIO.setup(27,GPIO.OUT)

# PWM=GPIO.PWM(26,50) #set 50Hz PWM output at GPIO26


# # RFID setup
# GPIO.setup(buzzer, GPIO.OUT)
# reader = SimpleMFRC522()

# Read RFID database
with open("authlist.txt", "r") as f:
    auth = f.read().splitlines()
    

def generate_steps_taken():
    # Generate random number of steps taken between 0 and 20000
    fake_steps_taken = random.randint(0, 20000)
    return fake_steps_taken

def generate_distance_travelled():
    # Generate random distance travelled between 0 and 20 km
    fake_distance_travelled = round(random.uniform(0, 20), 2)
    return fake_distance_travelled

def generate_temperature():
    # Generate random temperature between 20 and 40 degrees Celsius
    fake_temperature = round(random.uniform(25, 27), 2)
    return fake_temperature

def generate_humidity():
    # Generate random humidity between 0 and 100%
    fake_humidity = round(random.uniform(0, 100), 2)
    return fake_humidity

def generate_heart_rate():
    # Generate random heart rate between 60 and 100 bpm
    fake_heart_rate = random.randint(60, 100)
    return fake_heart_rate


def calculate_steps(distance_traveled, average_distance_per_step=0.762):
    steps = float(distance_traveled / average_distance_per_step)
    return steps

start_time = time.time()
buzz_duration = 1
while True:
    # Generate fake temperature and humidity data
    temperature, humidity = generate_temperature(), generate_humidity()

    # Generate fake heart rate
    heart_rate = generate_heart_rate()

    print(temperature, humidity)

    steps = generate_steps_taken()
    
    distance_travelled = generate_distance_travelled()

    elapsed_time = time.time() - start_time

    # Data to send to ThingSpeak
    resp = requests.get("https://api.thingspeak.com/update?api_key=FPC7UEB6NHIZXH0O&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s" % (heart_rate, steps, temperature, humidity, distance_travelled))
    result = json.loads(resp.text)

    if temperature > 30.0:
        message = f"Careful, it's hot out today! The temperature is {temperature}°C."
        # url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        url = f"https://api.telegram.org/bot{token}/getUpdates"
        print(requests.get(url).json())
        
    sleep(5)


    
    
# To do list:
'''
check rpi gpio import
check data input for thingspeak
distance calculation

login for flask
points system possibly?
if uw can make a ai model in order to detect whether the person is in the healthy range and stuff
i can also host onto render if needed
'''
