import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "GPIO morse code" )

def pulse( pin_nr, high_time, low_time ):
    GPIO.output(pin_nr, GPIO.HIGH)
    time.sleep(high_time)
    GPIO.output(pin_nr, GPIO.LOW)
    time.sleep(low_time)

def morse( pin_nr, dot_length, text ):
        for char in text:
            if char == ".":
                GPIO.output(pin_nr, GPIO.HIGH)
                time.sleep(dot_length)
                GPIO.output(pin_nr, GPIO.LOW)
                time.sleep(dot_length * 2)
            elif char == "-":
                GPIO.output(pin_nr, GPIO.HIGH)
                time.sleep(dot_length * 3)
                GPIO.output(pin_nr, GPIO.LOW)
                time.sleep(dot_length * 2)
            elif char == " ":
                GPIO.output(pin_nr, GPIO.LOW)
                time.sleep(dot_length * 3)

led = 18
GPIO.setup( led, GPIO.OUT )
morse( 18, 0.2, ".--. -.-- - .... --- -." )

