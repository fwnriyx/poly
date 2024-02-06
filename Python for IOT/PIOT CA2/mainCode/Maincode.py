import RPi.GPIO as GPIO
import I2C_LCD_driver
from time import sleep
from mfrc522 import SimpleMFRC522

# Constants for keypad and RFID modes
KEYPAD_MODE = 1
RFID_MODE = 2
RUN_MODE = 3

# Initialize variables
mode = ''
buzzer = 18
counter = 0
num = ''
secretkey = '123456'
auth = []

# LCD
LCD = I2C_LCD_driver.lcd()

#GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

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

def keypad_entry():
    global num, counter, secretkey
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
    if num == secretkey:
        print('Unlocked')
        LCD.lcd_clear()
        LCD.lcd_display_string('Unlocked!', 1)
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
        keypad_entry()
    elif mode == RFID_MODE:
        rfid_entry()
