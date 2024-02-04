"""
Run this scrupt on a computer (e.g. Laptop, Raspberry Pi)
"""

import serial
from time import sleep

# SETUP
ser = serial.Serial('/dev/ttyACM0', 115200)  # pico board is at /dev/ttyACM0
msg = "Hello from computer"
msg_id = 0

# LOOP
while True:
    data_tx = msg + f", {msg_id}\n"
    ser.write(bytes(data_tx.encode('utf-8')))  # transmit data
    if ser.inWaiting() > 0:
        data_rx = ser.readline()  # receive data
        data_rx = data_rx.decode("utf-8","ignore")
        print (data_rx)
    sleep(1)  # transmit "data_tx" and receive "data_rx" every second
    msg_id += 1  # increment message index by 1
