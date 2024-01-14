

import RPi.GPIO as GPIO
import I2C_LCD_driver
from time import sleep
from mfrc522 import SimpleMFRC522

buzzer = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzzer, GPIO.OUT)
reader = SimpleMFRC522()
auth = []

lcd = I2C_LCD_driver.lcd()

MATRIX = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          ['*', 0, '#']]  # layout of keys on keypad
secretkey = '123456'
counter = 0
num = ''
ROW = [6, 20, 19, 13]  # row pins
COL = [12, 5, 16]  # column pins

for i in range(3):
    GPIO.setup(COL[i], GPIO.OUT)
    GPIO.output(COL[i], 1)

for j in range(4):
    GPIO.setup(ROW[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)

runprogram = True

while True:
    lcd.lcd_clear()
    lcd.lcd_display_string('1 for RFID', 1)
    lcd.lcd_display_string('2 for password', 2)
    for i in range(3):  # loop thru’ all columns
        GPIO.output(COL[i], 0)  # pull one column pin low
        for j in range(4):  # check which row pin becomes low
            if GPIO.input(ROW[j]) == 0:  # if a key is pressed
                print(MATRIX[j][i])
                if MATRIX[j][i] == 1:
                    lcd.lcd_clear()
                    lcd.lcd_display_string("Put Tag", 1, 1)
                    id = reader.read_id()
                    id = str(id)
                    with open("authlist.txt", "r+") as f:
                        auth = f.read()
                    if id in auth:
                        number = auth.split('\n')
                        pos = number.index(id)
                        print("Card with UID", id, "found in database entry #", pos, "; access granted")
                        lcd.lcd_display_string("Success!", 1, 1)
                        GPIO.output(buzzer, GPIO.HIGH)
                        sleep(0.5)
                        GPIO.output(buzzer, GPIO.LOW)
                    else:
                        print("Card with UID", id, "not found in database; access denied")
                        lcd.lcd_clear()
                        lcd.lcd_display_string("Denied!", 1, 1)
                        GPIO.output(buzzer, GPIO.HIGH)
                        sleep(0.5)
                        GPIO.output(buzzer, GPIO.LOW)
                elif MATRIX[j][i] == 2:
                    counter = 0
                    num = ''
                    runprogram = True
                    while runprogram:
                        for x in range(3):  # loop thru’ all columns in keypad mode
                            GPIO.output(COL[x], 0)  # pull one column pin low
                            for y in range(4):  # check which row pin becomes low
                                if GPIO.input(ROW[y]) == 0:  # if a key is pressed
                                    if MATRIX[y][x] == '#':
                                        counter = 1
                                    else:
                                        num += str(MATRIX[y][x])
                                        lcd.lcd_clear()
                                        lcd.lcd_display_string('Password:', 1)
                                        lcd.lcd_display_string(num, 2)
                                        print('password = ' + num)
                                    while GPIO.input(ROW[y]) == 0:  # debounce
                                        sleep(0.1)
                            GPIO.output(COL[x], 1)  # write back default value of 1
                            if counter == 1:
                                lcd.lcd_clear()
                                if num == secretkey:
                                    print('unlocked')
                                    lcd.lcd_display_string('Unlocked!', 1)
                                    runprogram = False
                                    break
                                else:
                                    print('wrong password. Try again')
                                    lcd.lcd_display_string('Try again!', 1)
                                    counter = 0
                                    num = ''
