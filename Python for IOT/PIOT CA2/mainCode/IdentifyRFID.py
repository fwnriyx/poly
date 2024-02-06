import RPi.GPIO as GPIO
import I2C_LCD_driver
from time import sleep
import sys
from mfrc522 import SimpleMFRC522

#buzzer pin
buzzer = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzzer,GPIO.OUT)
reader = SimpleMFRC522()
auth = []

#LCD
lcd = I2C_LCD_driver.lcd()

while True:
        print("Hold card near the reader to check if it is in the database")
        lcd.lcd_clear()
        lcd.lcd_display_string("Put Tag",1,1)
        id = reader.read_id()
        id = str(id)
        f = open("authlist.txt", "r+")
        if f.mode == "r+":
              auth=f.read()
        if id in auth:
              number = auth.split('\n')
              pos = number.index(id)
              print("Card with UID", id, "found in database entry #", pos, "; access granted")
              lcd.lcd_display_string("Success!",1,1)
              GPIO.output(buzzer,GPIO.HIGH)
              sleep(0.5)
              GPIO.output(buzzer,GPIO.LOW)

        else:
              print("Card with UID", id, "not found in database; access denied")
              lcd.lcd_clear()
              lcd.lcd_display_string("Denied!",1,1)
              GPIO.output(buzzer,GPIO.HIGH)
              sleep(0.5)
              GPIO.output(buzzer,GPIO.LOW)
        sleep(2)
