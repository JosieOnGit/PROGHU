import RPi.GPIO as GPIO
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "input copy" )

led = 18
powerOn = 23
powerOff = 24

GPIO.setup( led, GPIO.OUT )
GPIO.setup( powerOn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
GPIO.setup(powerOff, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
   if( GPIO.input(powerOn) ):
      GPIO.output( led, GPIO.HIGH )
   elif(GPIO.input(powerOff)):
      GPIO.output( led, GPIO.LOW )
