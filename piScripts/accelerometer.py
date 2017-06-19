from RPi import GPIO as GPIO
from DbClass import DbClass
import time
import spidev
import os

miso = 9
mosi = 10
sclk = 11
DS = 5
STCP = 20
SHCP = 23
delay = 10**-7
spi = spidev.SpiDev()
spi.open(0, 1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DS, GPIO.OUT)
GPIO.output(DS, GPIO.LOW)
GPIO.setup(STCP, GPIO.OUT)
GPIO.output(STCP, GPIO.LOW)
GPIO.setup(SHCP, GPIO.OUT)
GPIO.output(SHCP, GPIO.LOW)

def writeOneByte(bytewaarde):
   GPIO.output(DS, bytewaarde)
   time.sleep(delay)
   GPIO.output(SHCP,GPIO.HIGH)
   time.sleep(delay)
   GPIO.output(SHCP,GPIO.LOW)

def copyToStorageRegister():
    GPIO.output(STCP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(STCP, GPIO.LOW)

def ReadChannel():
    adc = spi.xfer2([1, 26, 4])
    data = ((adc[1]&3)<<8) | adc[2]
    return adc
try:
    while True:
        print(ReadChannel())
except KeyboardInterrupt:
    spi.close()