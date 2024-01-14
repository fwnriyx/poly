import RPi.GPIO as GPIO
import I2C_LCD_driver
from time import sleep

LCD = I2C_LCD_driver.lcd()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

MATRIX=[ [1,2,3],
         [4,5,6],
         [7,8,9],
         ['*',0,'#']] #layout of keys on keypad
secretkey = '123456'
counter = 0
num = ''
ROW=[6,20,19,13] #row pins
COL=[12,5,16] #column pins

#set column pins as outputs, and write default value of 1 to each
for i in range(3):
    GPIO.setup(COL[i],GPIO.OUT)
    GPIO.output(COL[i],1)

#set row pins as inputs, with pull up
for j in range(4):
    GPIO.setup(ROW[j],GPIO.IN,pull_up_down=GPIO.PUD_UP)

#scan keypad
runprogram = True
while (runprogram):
    for i in range(3): #loop thru’ all columns
        GPIO.output(COL[i],0) #pull one column pin low
        for j in range(4): #check which row pin becomes low
            if GPIO.input(ROW[j])==0: #if a key is pressed
                if MATRIX[j][i] == '#':
                    counter = 1
                else:
                    num += str(MATRIX[j][i])
                    LCD.lcd_clear()
                    LCD.lcd_display_string('Password:', 1)
                    LCD.lcd_display_string(num, 2)
                    #print (MATRIX[j][i]) #print the key pressed
                    print('password = ' + num)
                    #print('counter=', counter)
                #print(MATRIX[j][i])
                while GPIO.input(ROW[j])==0: #debounce
                    sleep(0.1)
        GPIO.output(COL[i],1) #write back default value of 1
        if counter == 1:
            LCD.lcd_clear()
            if num == secretkey:
                print('unlocked')
                LCD.lcd_display_string('Unlocked!', 1)
                runprogram = False
                break
            else:
                print('wrong password. Try again')
                LCD.lcd_display_string('Try again!')
            counter = 0
            num = ''