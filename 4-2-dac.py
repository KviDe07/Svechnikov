import RPi.GPIO as gpio
import sys
from time import sleep


dac = [8, 11, 7, 1, 0, 5, 12, 6]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def decimal2bin(a, n):
    return [int(elem) for elem in bin(a)[2:].zfill(n)]

try:
    while (True):
        period = input('period')
        if not period.isdigit():
            print ('input a number')
            sys.exit()
        t = int(period) / 512
        for i in range (256):
            gpio.output(dac, decimal2bin(i, 8))
            sleep (t)
        for i in range (255, -1, -1):
            gpio.output(dac, decimal2bin(i, 8))
            sleep (t)
finally:
    gpio.output(dac, 0)
    gpio.cleanup()

        