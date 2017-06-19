from RPi import GPIO as GPIO
from DbClass import DbClass
import time
GPIO.setmode(GPIO.BCM)

#answer buttons
answerA = 21
answerB = 26
answerC = 19
answerD = 13
answerButtons = [21, 26 , 19, 13]

#answer buttons
for x in range(0,4):
    GPIO.setup(answerButtons[x], GPIO.IN, pull_up_down=GPIO.PUD_UP)

def readAnswerButtons():
    while True:
        print("answer1: " + str(GPIO.input(answerButtons[0])))
        print("answer2: " + str(GPIO.input(answerButtons[1])))
        print("answer3: " + str(GPIO.input(answerButtons[2])))
        print("answer4: " + str(GPIO.input(answerButtons[3])))

readAnswerButtons()