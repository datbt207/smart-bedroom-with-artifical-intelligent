import tensorflow
import pandas as pd
from tensorflow import keras
from keras import Sequential
from keras.layers import Activation, Dense


model = Sequential()
model.add(Dense(16, input_dim = 1, activation = "relu"))
model.add(Dense(32, activation = "relu"))
model.add(Dense(64, activation = "relu"))
model.add(Dense(1))
model.summary()

model.compile(optimizer='adam', loss='mean_squared_error',  metrics=['accuracy'])

def time_format(hour, minute):
    now = hour + minute/60
    return now

df = pd.read_csv("dataset.csv", on_bad_lines='skip')

hour = df.hour
minute = df.minute
temperature = df.temp

hour.to_numpy()
minute.to_numpy()
temperature.to_numpy()

time = []
temp = []
for i in range(259193):
    time.append(time_format(hour[i], minute[i]))
    temp.append(temperature[i])


model.fit(time, temp, epochs = 20, batch_size = 500)

model.save("model.hdf5")