from RPi import GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#knoppen declareren
buttons = [17, 24, 16, 22] #oranje, groen, blauw, rood
buttonOrange = 17
buttonGreen = 24
buttonBlue = 16
buttonRed = 22
valueReadButtons = [10, 10, 10, 10]

#leds declareren
leds = [27, 25, 18, 6] #oranje, groen, blauw, rood
ledOrange = 27
ledGreen = 25
ledBlue = 18
ledRed = 6

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