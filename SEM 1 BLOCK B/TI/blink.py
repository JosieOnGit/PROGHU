import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "GPIO blink" )

GPIO.setup( 18, GPIO.OUT )
while True:
   GPIO.output( 18, GPIO.HIGH )
   time.sleep( 0.5 )
   GPIO.output( 18, GPIO.LOW )
   time.sleep( 0.5 )
