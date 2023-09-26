import RPi.GPIO as gpio


dac = [8, 11, 7, 1, 0, 5, 12, 6]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
gpio.setup(21, gpio.OUT)

pwm = gpio.PWM(21, 1000)
pwm.start(0)

try: 
    while(True):
        DutyCicle = int(input())
        pwm.ChangeDutyCycle(DutyCicle)
        print ("{:.2f}".format(DutyCicle*3.3/100))

finally:
    gpio.output(dac, 0)
    gpio.output(21, 0)
    gpio.cleanup()