# IoT26-HW03_SeolJaemin.py
# 202234900 Seol Jaemin

from gpiozero import Button, MotionSensor
from picamera2 import Picamera2
import libcamera
from time import sleep
from signal import pause
import os

# create objects
# I swapped these two pins for convenience
button = Button(4) # GPIO 4 = pin 7
pir = MotionSensor(17) # GPIO 17 = pin 11

# Cam setup
cam = Picamera2()
config = cam.create_still_configuration()

# Flip Camera
config["transform"] = libcamera.Transform(vflip=1, hflip=1)
cam.configure(config)

# Start cam and make folder
cam.start()
path = f'~/Desktop/images'
path = os.path.expanduser(path)
os.makedirs(path, exist_ok=True)

i = 0 # image name

print("Running...")

# function to stop camera and program
def stop_camera():
    cam.stop()
    print("Stopping...")
    os._exit(0)

# function to take photo
def take_photo():
    global i
    i += 1

    # set path
    path = f'~/Desktop/images/image_{i}.jpg'
    path = os.path.expanduser(path)
    cam.capture_file(path)
    print("A photo has been taken")
    
    # Cool down
    for j in range(5, 0, -1):
        print(f"Cooldown: {j}")
        sleep(1)
    print("Ready")

# assign functions to button and motion sensor
button.when_pressed = stop_camera
pir.when_motion = take_photo

pause()