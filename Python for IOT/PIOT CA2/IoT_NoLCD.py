# import RPi.GPIO as GPIO
import RPi.GPIO as GPIO
# import I2C_LCD_driver
from time import sleep
from mfrc522 import SimpleMFRC522
import os
import requests
import json
from PIL import Image
from io import BytesIO
from mainCode.adxl345 import ADXL345
import random
import dht11
import time    
import telegram

# heart_rate = [52,50,51,53,55,57,58]

token = "6236591816:AAEAP8PT7j7PE-bCsrHkz4QtVqQtZOquK9Y"
url = f"https://api.telegram.org/bot{token}/getUpdates"
chat_id = "6236591816"


# Constants for keypad and RFID modes
RFID_MODE = 1
FITNESS_MODE = 2
accelerometer = ADXL345(i2c_port=1, address=0x53)

current_dir = os.getcwd()

# Initialize variables
mode = ''
buzzer = 18
counter = 0
num = ''
auth = []

#GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#servo motor
GPIO.setmode(GPIO.BCM) #choose BCM mode
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT) #set GPIO 26 as output

PWM=GPIO.PWM(26,50) #set 50Hz PWM output at GPIO26


# RFID setup
GPIO.setup(buzzer, GPIO.OUT)
reader = SimpleMFRC522()

# Read RFID database
with open("authlist.txt", "r") as f:
    auth = f.read().splitlines()

def get_dht11_data():
    instance = dht11.DHT11(pin=21)
    result = instance.read()
    if result.is_valid():
        temperature = result.temperature
        humidity = result.humidity
        return temperature, humidity
    else:
        return None, None
    

def generate_heart_rate():
    # Generate random or predefined fake data for testing
    fake_heart_rate = random.randint(60, 100)

    return fake_heart_rate


def calculate_steps(distance_traveled, average_distance_per_step=0.762):
    steps = float(distance_traveled / average_distance_per_step)
    return steps

start_time = time.time()
buzz_duration = 1
while True:
    GPIO.setup(27,GPIO.OUT)
    # Get accelerometer data
    x, y, z = accelerometer.get_3_axis_adjusted()
    print(x,y,z)
    # Assuming 'z' is the vertical (up-down) acceleration
    current_velocity = 0
    current_displacement = 0
    vertical_acceleration = z
    time_step = 0.1
    # Integrate acceleration to get velocity
    current_velocity += vertical_acceleration * time_step

    # Integrate velocity to get displacement (distance traveled)
    current_displacement += current_velocity * time_step

    # Get accelerometer data, temp and humidity from dht11
    temperature, humidity = get_dht11_data()
    #random generate heart rate
    heart_rate = generate_heart_rate()
    print(temperature, humidity)
        # Calculate steps based on distance traveled
    dist_travelled = current_displacement  # Assuming you have a function for distance
    steps = calculate_steps(dist_travelled)
    elapsed_time = time.time() - start_time
    # Data to send to ThingSpeak
    resp = requests.get("https://api.thingspeak.com/update?api_key=FPC7UEB6NHIZXH0O&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s" % (heart_rate, steps, temperature, humidity, current_displacement))
    result = json.loads(resp.text)
    if temperature > 30.0:
        message = f"Careful, it's hot out today! The temperature is {temperature}°C."
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url).json())
        


    
    
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
