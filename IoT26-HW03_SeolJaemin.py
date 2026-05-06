# IoT26-HW03_SeolJaemin.py
# 202234900 Seol Jaemin

from gpiozero import Button, MotionSensor
from picamera2 import Picamera2
import libcamera
from time import sleep
from signal import pause
import os.path

# create objects
# I swapped these two pins for convenience
button = Button(4) # GPIO 4 = pin 7
pir = MotionSensor(2) # GPIO 2 = pin 3

# Cam setup
cam = Picamera2()
config = cam.create_still_configuration()

# Flip Camera
config["transform"] = libcamera.Transform(vflip=1)
cam.configure(config)

# Start cam
cam.start()

i = 0 # image name

# function to stop camera and program
def stop_camera():
    cam.stop()
    print("Stopping...")
    exit()

# function to take photo
def take_photo():
    global i
    i += 1

    # set path
    path = f'~/Desktop/image_{i}.jpg'
    path = os.path.expanduser(path)
    cam.capture_file(path)
    print("A photo has been taken")
    sleep(5)

# assign functions to button and motion sensor
button.when_pressed = stop_camera
pir.when_motion = take_photo

pause()