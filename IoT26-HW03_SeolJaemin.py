# IoT26-HW03_SeolJaemin.py
# 202234900 Seol Jaemin

from gpiozero import Button, MotionSensor
from picamera import PiCamera
from time import sleep
from signal import pause
import os.path

# create objects
button = Button(2) # GPIO 2 = pin 3
pir = MotionSensor(4) # GPIO = pin 7
camera = PiCamera()

# Start cam
camera.rotation = 180 # Based on camera's physical orientation
camera.start_preview()

i = 0 # image name

# function to stop camera and program
def stop_camera():
    camera.stop_preview()
    exit()

# function to take photo
def take_photo():
    global i
    i += 1
    # set path
    path = f'~/Desktop/image_{i}.jpg'
    path = os.path.expanduser(path)
    camera.capture(path)
    print("A photo has been taken")
    sleep(10)

# assign functions to button and motion sensor
button.when_pressed = stop_camera
pir.when_motion = take_photo

pause()