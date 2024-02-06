# import RPi.GPIO as GPIO
import RPi.GPIO as GPIO
import I2C_LCD_driver
from time import sleep
from mfrc522 import SimpleMFRC522
from picamera import PiCamera
import dht11
import os
import requests
import json
import telegram
from PIL import Image
from io import BytesIO
from mainCode.dht11_example import DHT11
from mainCode.adxl345 import ADXL345
import random


heart_rate = [52,50,51,53,55,57,58]

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

# LCD
LCD = I2C_LCD_driver.lcd()

#GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#servo motor
GPIO.setmode(GPIO.BCM) #choose BCM mode
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT) #set GPIO 26 as output

PWM=GPIO.PWM(26,50) #set 50Hz PWM output at GPIO26

# Keypad setup
MATRIX = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          ['*', 0, '#']]
ROW = [6, 20, 19, 13]
COL = [12, 5, 16]

#set column pins as outputs, and write default value of 1 to each
for i in range(3):
    GPIO.setup(COL[i],GPIO.OUT)
    GPIO.output(COL[i],1)

#set row pins as inputs, with pull up
for j in range(4):
    GPIO.setup(ROW[j],GPIO.IN,pull_up_down=GPIO.PUD_UP)

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
    

def generate_fake_data():
    # Generate random or predefined fake data for testing
    fake_heart_rate = random.randint(50, 100)
    fake_steps = random.randint(100, 500)
    fake_temperature = random.uniform(20.0, 30.0)  # Random float between 20.0 and 30.0
    fake_humidity = random.uniform(30.0, 60.0)  # Random float between 30.0 and 60.0
    fake_distance = random.uniform(0.0, 10.0)  # Random float between 0.0 and 10.0

    return fake_heart_rate, fake_steps, fake_temperature, fake_humidity, fake_distance


def calculate_steps(distance_traveled, average_distance_per_step=0.762):
    steps = distance_traveled / average_distance_per_step
    return steps


def keypad_entry(secretkey):
    print(secretkey)
    global num, counter
    LCD.lcd_clear()
    LCD.lcd_display_string('Enter pass:', 1)
    while counter == 0:  # Wait until the complete password is entered
        for i in range(3):  # Loop through all columns
            GPIO.output(COL[i], 0)  # Pull one column pin low
            for j in range(4):  # Check which row pin becomes low
                if GPIO.input(ROW[j]) == 0:  # If a key is pressed
                    if MATRIX[j][i] == '#':
                        counter = 1
                    else:
                        num += str(MATRIX[j][i])
                        LCD.lcd_clear()
                        LCD.lcd_display_string('Password:', 1)
                        LCD.lcd_display_string(num, 2)
                    while GPIO.input(ROW[j]) == 0:  # Debounce
                        sleep(0.1)
            GPIO.output(COL[i], 1)  # Write back default value of 1

    # At this point, the complete password has been entered
    
    if int(num) == secretkey:
        PWM.start(3) #13% duty cycle
        print('Unlocked')
        LCD.lcd_clear()
        LCD.lcd_display_string('Logged in!', 1)
        sleep(2) #allow time for movement
        PWM.start(12) #13% duty cycle
        sleep(2)
    else:
        print('Wrong password. Try again')
        LCD.lcd_clear()
        LCD.lcd_display_string('Try again!', 1)
    sleep(1)
    counter = 0
    num = ''

def rfid_entry():
    global auth
    print("Hold card near the reader to check if it is in the database")
    LCD.lcd_clear()
    LCD.lcd_display_string("Put Tag", 1, 1)
    id, text = reader.read()
    id = str(id)
    if id in auth:
        pos = auth.index(id)
        print("Card with UID", id, "found in database entry #", pos, "; access granted")
        LCD.lcd_display_string("Success!", 1, 1)
        GPIO.output(buzzer, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(buzzer, GPIO.LOW)
        PWM.start(3)
        sleep(2) #allow time for movement
        PWM.start(12) #13% duty cycle
        sleep(2)
        
    else:
        print("Card with UID", id, "not found in database; access denied")
        LCD.lcd_clear()
        LCD.lcd_display_string("Denied!", 1, 1)
        GPIO.output(buzzer, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(buzzer, GPIO.LOW)
    sleep(2)

def get_keypad_input():
    # This function reads the keypad input and returns the pressed key, or None if no key is pressed
    for i in range(3):  # Loop through all columns
        GPIO.output(COL[i], 0)  # Pull one column pin low
        for j in range(4):  # Check which row pin becomes low
            if GPIO.input(ROW[j]) == 0:  # If a key is pressed
                while GPIO.input(ROW[j]) == 0:  # Debounce
                    sleep(0.1)
                return MATRIX[j][i]
        GPIO.output(COL[i], 1)  # Write back default value of 1
    return None

while True:
    LCD.lcd_clear()
    LCD.lcd_display_string('Enter 1 for RFID', 1, 0)
    LCD.lcd_display_string('Enter 2 for Fitness mode', 2, 0)
    choice = None
    while not choice:
        choice = get_keypad_input()
    if choice == 1:
        mode = RFID_MODE
    elif choice == 2:
        mode = FITNESS_MODE
    # Get accelerometer data
    x, y, z = accelerometer.get_3_axis_adjusted()

    # Assuming 'z' is the vertical (up-down) acceleration
    current_velocity = 0
    current_displacement = 0
    vertical_acceleration = z
    time_step = 0.1
    # Integrate acceleration to get velocity
    current_velocity += vertical_acceleration * time_step

    # Integrate velocity to get displacement (distance traveled)
    current_displacement += current_velocity * time_step
    if mode == FITNESS_MODE:
        # Get accelerometer data
        x, y, z = accelerometer.get_3_axis_adjusted()

        # Get temperature and humidity data from DHT11
        temperature, humidity = get_dht11_data()

        # Calculate steps based on distance traveled
        dist_travelled = current_displacement  # Assuming you have a function for distance
        steps = calculate_steps(dist_travelled)
        heart_rate, steps, temperature, humidity, current_displacement = generate_fake_data()
        # Data to send to ThingSpeak
        resp = requests.get("https://api.thingspeak.com/update?api_key=FPC7UEB6NHIZXH0O&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s" % (heart_rate, steps, temperature, humidity, current_displacement))
        result = json.loads(resp.text)

    elif mode == RFID_MODE:
        rfid_entry()

        