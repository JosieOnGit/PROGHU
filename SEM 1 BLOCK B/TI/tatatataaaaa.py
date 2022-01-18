
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

print("GPIO pulse")


def highBlink(pin_nr, high_on, high_sleep):
    GPIO.output(pin_nr, GPIO.HIGH)
    time.sleep(high_on)
    GPIO.output(pin_nr, GPIO.LOW)
    time.sleep(high_sleep)


def pulse(pin_nr, high_on, high_sleep, low_on, low_sleep):
    highBlink(pin_nr, high_on, high_sleep)
    highBlink(pin_nr, high_on, high_sleep)
    highBlink(pin_nr, high_on, high_sleep)
    GPIO.output(pin_nr, GPIO.HIGH)
    time.sleep(low_on)
    GPIO.output(pin_nr, GPIO.LOW)
    time.sleep(low_sleep)


led = 18
GPIO.setup(led, GPIO.OUT)
while True:
    pulse(led, 0.2, 0.2, 0.7, 0.2)
