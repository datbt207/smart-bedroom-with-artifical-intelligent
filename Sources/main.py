from time import sleep
from therm import *
from lcd import *
from button import *
from actuator import *
import tensorflow as tf
import datetime

model = tf.keras.models.load_model("model.hdf5")

def time_now():
    now = datetime.datetime.now()
    return now.hour + now.minute/60

while True:
    while not get_auto_state():
        temp = read_temp()
        lcd.clear()
        temp_print(temp)
    while get_auto_state():
        temp = read_temp()
        auto_temp = model.predict([time_now()])
        lcd.clear()
        temp_print(temp)
        auto_print(auto_temp[0][0])
        if auto_temp < temp :
            fan_on()
        else:
            fan_off()