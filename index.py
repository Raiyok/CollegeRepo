import time
import picamera
import RPi.GPIO as gpio

# Pin Definitions
m11=17
m12=27
button=19

# GPIO Setup
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(m11,gpio.OUT)
gpio.setup(m12,gpio.OUT)
gpio.setup(button,gpio.IN)

# Initial State
gpio.output(m11,0)
gpio.output(m12,0)

def capture_image():
    camera.resolution=(1280,720)
    camera.start_preview()
    time.sleep(2)
    camera.capture('/home/pi/Pictures/myimg.jpg')
    camera.stop_preview()
    print('done')

def gate():
    gpio.output(m11,1)
    gpio.output(m12,0)
    time.sleep(1.5)
    gpio.output(m11,0)
    gpio.output(m12,0)
    time.sleep(3)
    gpio.output(m11,0)
    gpio.output(m12,1)
    time.sleep(1.5)
    gpio.output(m11,0)
    gpio.output(m12,0)
    time.sleep(2)

# Camera Initialization
time.sleep(1)
camera=picamera.PiCamera()
camera.rotation=180
camera.awb_mode='auto'
camera.brightness=55
time.sleep(2)

# Main Loop
while 1:
    print('Press button to capture image')
    if gpio.input(button)==0:
        capture_image()
        gate()
        time.sleep(0.5)
        
