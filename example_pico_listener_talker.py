"""
Run this script on Pico board
"""

import sys
import select


# SETUP
poller = select.poll()
poller.register(sys.stdin, select.POLLIN)
event = poller.poll()
while True:
    for msg, _ in event:
        data_rx = msg.readline().rstrip()  # receive data
        print(data_rx)  # IMPORTANT: this line will transmit "data_rx" to computer if not running in Thonny
