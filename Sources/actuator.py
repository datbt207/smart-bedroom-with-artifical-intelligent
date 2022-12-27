import RPi.GPIO as GPIO
from time import sleep
from therm import *
from lcd import *

#LAMP_PIN 5
#FAN_PIN 3
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

lamp_state = 0
fan_state = 0
auto_state = 0


def lamp_on():
    global lamp_state
    lamp_state = 1
    GPIO.output(5, GPIO.LOW)

def lamp_off():
    global lamp_state
    lamp_state = 0
    GPIO.output(5, GPIO.HIGH)

def fan_on():
    global fan_state
    GPIO.output(3, GPIO.LOW)
    fan_state = 1
def fan_off():
    global fan_state
    fan_state = 0
    GPIO.output(3, GPIO.HIGH)

def lamp_act():
    global lamp_state
    if not lamp_state:
        lamp_on()
    else:
        lamp_off()

def fan_act():
    global fan_state
    if not fan_state:
        fan_on()
    else:
        fan_off()

def auto_act():
    global auto_state
    if auto_state:
        auto_state = 0
    else:
        auto_state = 1

def get_auto_state():
    global auto_state
    return auto_state