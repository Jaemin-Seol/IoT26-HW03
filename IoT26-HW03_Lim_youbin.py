#Lim_youbin
#picamera2
from gpiozero import Button, MotionSensor
from picamera2 import Picamera2
from time import sleep
from signal import pause

button = Button(2)
pir = MotionSensor(4)

#setting camera
camera = Picamera2()
camera_config = camera.create_still_configuration()
camera.configure(camera_config)

camera.start()

i = 0

def stop_camera():
    camera.stop()
    print("Camera stopped")
    exit()

def take_photo():
    global i
    i += 1

    file_path = f'/home/iot3_user/Desktop/image_{i}.jpg'
    camera.capture_file(file_path)

    print('A photo has been taken')
    # waiting for no motion
    pir.wait_for_no_motion()
    sleep(5)

button.when_pressed = stop_camera
pir.when_motion = take_photo

pause()
