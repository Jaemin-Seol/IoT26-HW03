from gpiozero import Button, MotionSensor
from picamera2 import Picamera2
from time import sleep
from signal import pause
import sys

button = Button(2)
pir = MotionSensor(4)
picam2 = Picamera2()

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

    filename = f"/home/iot3_user/Desktop/iot3/IoT26-HW03/images/image_{image_count}.jpg"
    picam2.capture_file(str(filename))

    print("motion detected, take picture")

    sleep(5)  

button.when_pressed = stop_program
pir.when_motion = take_photo

pause()
