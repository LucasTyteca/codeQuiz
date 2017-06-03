from RPi import GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#knoppen declareren
buttons = [18, 17, 27, 22] #oranje, rood, groen, blauw
buttonOrange = 18
buttonRed = 17
buttonGreen = 27
buttonBlue = 22
valueReadButtons = [10, 10, 10, 10]

#leds declareren
leds = [5, 6, 13, 19] #oranje, rood, groen, blauw
ledOrange = 5
ledRed = 6
ledGreen = 19
ledBlue = 26

#andere variabelen
notWon = True

#buttons setup
for x in range(0,4):
    GPIO.setup(buttons[x], GPIO.IN, pull_up_down=GPIO.PUD_UP)


#leds setup
for x in range(0,4):
    GPIO.setup(leds[x], GPIO.OUT)
    GPIO.output(leds[x], GPIO.HIGH)

def readButtons():
    for x in range(0,4):
        if GPIO.input(buttons[x]) == 0:
            return x
    return 9

while notWon == True:
    pushed = readButtons()
    if pushed != 9:
        GPIO.output(leds[pushed], GPIO.LOW)