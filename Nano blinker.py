import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
GPIO.output(10, GPIO.OUT)

try:
  while
    GPIO.output(10,GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.25)
except KeyboardInterrupt:
  gpio.cleanup()
    
