from picamera import PiCamera
import os
from time import sleep


current_dir = os.getcwd()

camera = PiCamera()
camera.capture(current_dir + "/static/intruderimage.jpg")

