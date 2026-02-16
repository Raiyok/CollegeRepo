import RPi.GPIO as GPIO
import time

# Motor pins
MOTOR_PIN1 = 17 # Clockwise
MOTOR_PIN2 = 27 # Anti-clockwise

# Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_PIN2, GPIO.OUT)

# Functions
def clockwise(duration=1.5):
    print(">>> CLOCKWISE")
    GPIO.output(MOTOR_PIN1, GPIO.HIGH)
    GPIO.output(MOTOR_PIN2, GPIO.LOW)
    time.sleep(duration)

def anticlockwise(duration=1.5):
    print(">>> ANTI-CLOCKWISE")
    GPIO.output(MOTOR_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_PIN2, GPIO.HIGH)
    time.sleep(duration)

def stop(duration=1):
    print(">>> STOP")
    GPIO.output(MOTOR_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_PIN2, GPIO.LOW)
    time.sleep(duration)

# Demo sequence
try:
    print("DC Motor Demo Starting...")
    
    for i in range(3):
        clockwise(1.5)
        stop(0.5)
        anticlockwise(1.5)
        stop(1)

    print("Demo complete!")

except KeyboardInterrupt:
    print("\nStopped by user")

finally: # must be lowercase
    GPIO.output(MOTOR_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_PIN2, GPIO.LOW)
    GPIO.cleanup()
    print("GPIO cleaned up")
