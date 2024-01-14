import RPi.GPIO as GPIO
from server import I2C_LCD_driver
from time import sleep
from mfrc522 import SimpleMFRC522
from picamera import PiCamera
import os
import requests
import json
import telegram
from PIL import Image
from io import BytesIO

# Constants for keypad and RFID modes
KEYPAD_MODE = 1
RFID_MODE = 2

#Camera
camera = PiCamera()
current_dir = os.getcwd()

def img_capture():
    camera.capture(current_dir + "/server/static/intruderimage.jpg")
    img_path = current_dir + "/server/static/intruderimage.jpg"
    sleep(5)
    # send img to tele
    TOKEN = "6044657815:AAGGrGvHPIDhKiayFyuNxmEUrjnVGTfGz3Y"
    chat_id = "837915524"
    message = "A user has opened door"
    # send message
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()
    # send img
    img = Image.open(img_path)
    
    image_stream = BytesIO()
    img.save(image_stream, format='JPEG')
    image_stream.seek(0)
    
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    files = {'photo': (img_path, image_stream)}
    data = {'chat_id': chat_id}
    requests.post(url, files=files, data=data).json()



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
with open(current_dir + "/server/authlist.txt", "r") as f:
    auth = f.read().splitlines()

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
        LCD.lcd_display_string('Unlocked!', 1)
        sleep(2) #allow time for movement
        PWM.start(12) #13% duty cycle
        sleep(2)
        img_capture()
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
        img_capture()
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
    LCD.lcd_display_string('Enter 1 for keypad', 1, 0)
    LCD.lcd_display_string('Enter 2 for RFID', 2, 0)
    choice = None
    while not choice:
        choice = get_keypad_input()
    if choice == 1:
        mode = KEYPAD_MODE
    elif choice == 2:
        mode = RFID_MODE

    if mode == KEYPAD_MODE:
        # data from thingspeak
        resp = requests.get("https://api.thingspeak.com\
/channels/2154521/fields/4.json?api_key=M2U4OL8SE4EJFLWV&results=1")
        result = json.loads(resp.text)
        lockMode = result["feeds"][0]["field4"]
        lockMode = int(lockMode)
        print(lockMode)
        
        if lockMode == 1:
            resp = requests.get("https://api.thingspeak.com\
/channels/2154521/fields/3.json?api_key=M2U4OL8SE4EJFLWV&results=1")
            result = json.loads(resp.text)
            otp = int(result["feeds"][0]["field3"])
            keypad_entry(otp)
        elif lockMode == 2:
            password = 12345
            keypad_entry(password)
    elif mode == RFID_MODE:
        rfid_entry()

