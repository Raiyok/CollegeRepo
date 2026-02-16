import time
import picamera
import RPi.GPIO as gpio

m11=17
m12=27
button=19

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(m11,gpio.OUT)
gpio.setup(m12,gpio.OUT)
gpio.setup(button,gpio.IN)

gpio.output(m11,0)
gpio.output(m12,0)

def capture_image():
    camera.resolution=(1280,720)
    camera.start_preview()
