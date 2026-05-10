# gpiozero: controls raspberrypi pins
from gpiozero import Button, MotionSensor
from picamera2 import Picamera2
from time import sleep
from signal import pause
import sys

# button assign gpio pin 2
button = Button(2)
# pir motion sensor gpio pin 4
pir = MotionSensor(4)
picam2 = Picamera2()

# still photo capture mode
config = picam2.create_still_configuration()
picam2.configure(config)

picam2.start()

image_count = 0

def stop_program():
    print("stop camera")
    picam2.stop()
    sys.exit(0)

def take_photo():
    global image_count

    image_count += 1

    # numbered jpg path
    filename = f"/home/iot3_user/Desktop/iot3/IoT26-HW03/images/image_{image_count}.jpg"
    picam2.capture_file(str(filename))

    print("motion detected, take picture")

    # cooldown before next capture
    sleep(5)

# stop camera on button press
button.when_pressed = stop_program
# take picture when pir sees motion
pir.when_motion = take_photo

# keeps the process alive while waiting for pin event
pause()
