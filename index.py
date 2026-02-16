import time
import picamera
import RPi.GPIO as GPIO

# Motor pins
m11 = 17
m12 = 27

# Button pin
button = 19

# GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(m11, GPIO.LOW)
GPIO.output(m12, GPIO.LOW)

# Create camera object
camera = picamera.PiCamera()

def capture_image():
    print("Capturing image...")
    camera.resolution = (1280, 720)
    camera.start_preview()
    time.sleep(2) # Allow camera to warm up
    camera.capture("/home/pi/image.jpg")
    camera.stop_preview()
    print("Image saved!")

try:
    print("Press button to capture image & run motor")

    while True:
        if GPIO.input(button) == GPIO.LOW: # Button pressed
            print("Button Pressed!")

            # Motor ON
            GPIO.output(m11, GPIO.HIGH)
            GPIO.output(m12, GPIO.LOW)

            capture_image()

            time.sleep(2)

            # Motor OFF
            GPIO.output(m11, GPIO.LOW)
            GPIO.output(m12, GPIO.LOW)

            time.sleep(1)

except KeyboardInterrupt:
    print("Stopped by user")

finally:
    GPIO.cleanup()
    camera.close()
    print("GPIO Cleaned")
