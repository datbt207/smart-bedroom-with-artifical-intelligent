# SMART BEDROOM WITH ARTIFICAL INTELLIGENT

## Introduction

With the requirement of designing a bedroom with buttons, we will be able to turn
off the lights and fans through the push button, and at the same time, we measure the
temperature through the DS18B20 sensor and display the temperature through the LCD.

When we turn on Auto mode via the push button, we have an AI model with auto
temperature output. It will compare the actual temperature with the model output
temperature so that the fan can be adjusted on and off accordingly.

When the temperature from the sensor is greater than the train data at the time of input
to the AI model, it will turn on the fan.

The operating system chosen to use is Raspberry Pi OS (formerly known as Raspbian)
is the introduction for the operating system for normal use on a Raspberry Pi

The operating system supports interfaces, good network communication, and good
support for languages in another topic.

A SD card writing tool that works on Mac Operating system, Ubuntu, and Windows
called Raspberry Pi Imager.

Hardware preparation:
Based on the requirements of the topic, we will choose the following hardware:

- Button: when the button is pressed, it will transmit a signal to the Raspberry for
control.
- Sensor: here is see a blocked sensor that will transfer the signal to raspberry, the signal
that is also the main signal to Raspberry to display the heat.
- LCD: Block display, this is the temperature display and if auto mode is on, it will
show the matching temperature pattern.
- LED: This is block led, then click the button, the signal from the matching raspberry,
bright led.
- FAN: block Fan when the button is pressed, there is a signal from the raspberry to
turn off the relay for the FAN to run. Another face, when on the auto mode, FAN will turn
on and off automatically based on the temperature.

## Function
The model has implemented the proposed features including intuitively controlling
the device with auto and non-auto modes and easily changing between the two with the
push of a button.
- For non-auto mode, the buttons have well recognized almost all operations during
use, including side actions such as holding the button or pressing continuously.
- For auto mode, the temperature signal recognition is continuous in parallel with the
adaptive temperature trained from the artificial intelligence model to adjust the fan to33
operate according to the end user needs. In auto mode, the button still keeps the Listen
mechanism for auto state switching and led on and off, but it won't be effective for fan
control.

The disadvantage of the experiment is that the delay in execution is still high, which
is caused by two main parts: the sequential programming method increases the execution
time of the instruction and the devices that use the delay time are quite high. in signal
conversion such as Temperature sensor and LCD overview increases system delayed

![image](https://user-images.githubusercontent.com/116724181/215951698-a13d2311-9490-45b8-a099-2a066fd8de75.png)


## Tool and Software

Raspberry Pi 4 board: here we focus on learning, studying how to install the operating
system, using the Raspberry Pi's Gpio pins, and also training the AI model on the raspberry.

Python programming language: we use python language throughout the process, and
it is the language used in the article to compile and train AI.

TensorFlow: we will learn TensorFlow at a basic level to understand and apply to the
topic.

Linux Operating System for Raspberry Pi: use to actually flow control in hardware system when coding and debuging

## Participate

  - [Developer] *Bùi Tuấn Đạt*
  
  - [Developer] *Trần Phan Bảo Khang*

## Additional Infomation

  - **Advisor:** PhD. *Truong Ngoc Son*
  
  - Ho Chi Minh City University of Technology and Education  
