import RPi.GPIO as GPIO
import I2C_LCD_driver
from time import sleep
import sys
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)
reader = SimpleMFRC522()
auth = []

#LCD object
lcd = I2C_LCD_driver.lcd()

while True:
        print("Hold card near the reader to register it in the database")
        lcd.lcd_display_string("Place your Tag",1,1)
        lcd.lcd_display_string("on the reader",2,1)
        id = reader.read_id()
        id = str(id)
        f = open("authlist.txt", "a+")
        f = open("authlist.txt", "r+")
        if f.mode == "r+":
              auth=f.read()
        if id not in auth:
              f.write(id)
              f.write('\n')
              f.close()
              pos = auth.count('\n')
              print("New card with UID", id,  "detected; registered as entry #", pos)
              lcd.lcd_clear()
              lcd.lcd_display_string("Tag ID:",1,5)
              lcd.lcd_display_string(str(id),2,1)
              
        else:
              number = auth.split('\n')
              pos = number.index(id)
              print("Card with UID", id, "already registered as entry #", pos)
              lcd.lcd_clear()
              lcd.lcd_display_string("Already",1,5)
              lcd.lcd_display_string("Registered!",2,3)
        sleep(2)

