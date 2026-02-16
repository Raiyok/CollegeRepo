
Ronit Teli <ronitteli1@gmail.com>
8:45 AM (2 minutes ago)
to me, Sahil

import RPi.GPIO as GPIO
import time

# Motor pins (BCM numbering)
MOTOR_PIN1 = 17 # Clockwise
MOTOR_PIN2 = 27 # Anti-clockwise

# Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(MOTOR_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_PIN2, GPIO.OUT)

# Initial stop
GPIO.output(MOTOR_PIN1, GPIO.LOW)
GPIO.output(MOTOR_PIN2, GPIO.LOW)


def clockwise(duration=2):
    print(">>> CLOCKWISE")
    GPIO.output(MOTOR_PIN1, GPIO.HIGH)
    GPIO.output(MOTOR_PIN2, GPIO.LOW)
    time.sleep(duration)
    stop()


def anticlockwise(duration=2):
    print(">>> ANTI-CLOCKWISE")
    GPIO.output(MOTOR_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_PIN2, GPIO.HIGH)
    time.sleep(duration)
    stop()


def stop():
    print(">>> STOP")
    GPIO.output(MOTOR_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_PIN2, GPIO.LOW)


# Test loop
try:
    while True:
        clockwise(3)
        time.sleep(1)

        anticlockwise(3)
        time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped")

finally:
    GPIO.cleanup()
