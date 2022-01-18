import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "servo wave" )

def pulse( pin_nr, delay1, delay2 ):
    GPIO.output(pin_nr, GPIO.HIGH)
    time.sleep(delay1)
    GPIO.output(pin_nr, GPIO.LOW)
    time.sleep(delay2)

def servo_pulse( pin_nr, position ):
    pulseB = ((position * 0.02) + 0.5) / 1000
    pulse(25, pulseB, 0.02)

   # implementeer deze functie

servo = 25
GPIO.setup( servo, GPIO.OUT )
while True:
   for i in range( 0, 100, 1 ):
      servo_pulse( servo, i )
   for i in range( 100, 0, -1 ):
      servo_pulse( servo, i )