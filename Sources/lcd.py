import os
import glob
import time
from RPLCD import CharLCD
import RPi.GPIO as GPIO

lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

def temp_print(temp):
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Temp: " + str(temp) + chr(223) + "C")
def auto_print(temp):
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Auto: " + str(temp) + chr(223) + "C")
