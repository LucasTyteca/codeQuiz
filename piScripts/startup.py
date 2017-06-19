from RPi import GPIO as GPIO
import time
from random import randint
GPIO.setmode(GPIO.BCM)
def startup():
    #leds declareren
    leds = [5, 6, 13, 19] #oranje, rood, groen, blauw

    #andere variabelen
    vorigRandom = 7

    #leds setup
    for x in range(0,4):
        GPIO.setup(leds[x], GPIO.OUT)

    try:
        while True:
            random = randint(0,3)
            while random == vorigRandom:
                random = randint(0,3)
            GPIO.output(leds[random], GPIO.HIGH)
            if vorigRandom != 7:
                GPIO.output(leds[vorigRandom], GPIO.LOW)
            vorigRandom = random
            time.sleep(0.5)
    except KeyboardInterrupt:
        for x in range(0,4):
            GPIO.output(leds[x], GPIO.LOW)

    GPIO.cleanup()

startup()