import RPi.GPIO as GPIO
from actuator import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# LAMP_BUTTON_PIN 11 
# FAN_BUTTON_PIN 13 
# AUTO_BUTTON_PIN 15

GPIO.setup(11, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, GPIO.PUD_DOWN)

def lamp_callback(channel):
    lamp_act()
    GPIO.remove_event_detect(11)
    lamp_detect()

def fan_callback(channel):
    fan_act()
    GPIO.remove_event_detect(13)
    fan_detect()
def auto_callback(channel):
    auto_act()
    GPIO.remove_event_detect(15)
    auto_detect()

def lamp_detect():
    GPIO.add_event_detect(11, GPIO.FALLING, callback = lamp_callback)

def fan_detect():
    GPIO.add_event_detect(13, GPIO.FALLING, callback = fan_callback)

def auto_detect():
    GPIO.add_event_detect(15, GPIO.FALLING, callback = auto_callback)

lamp_detect()
fan_detect()
auto_detect()

