#!/usr/bin/env python3

import os
import time

# Display a welcome message
print("Welcome to my Raspberry Pi script!")

# Get the current date and time
now = time.strftime("%Y-%m-%d %H:%M:%S")

# Display the current date and time
print("The current date and time is", now)

# Display the available disk space
print("The available disk space is:")
os.system("df -h")

# Display the CPU temperature
temp = os.popen("vcgencmd measure_temp").readline()
print("The CPU temperature is:", temp)

# Display the list of connected devices
print("The following devices are connected:")
os.system("lsusb")

# Display the IP address of the Raspberry Pi
ip_address = os.popen("hostname -I").readline().strip()
print("The IP address of the Raspberry Pi is:", ip_address)

# Display the system uptime
uptime = os.popen("uptime -p").readline().strip()
print("The system has been up for:", uptime)

# Display a farewell message
print("Thanks for using my Raspberry Pi script! Goodbye.")
