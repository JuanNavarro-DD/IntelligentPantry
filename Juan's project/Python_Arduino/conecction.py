import serial
import time

Arduino = serial.Serial(port="/dev/ttyUSB0", baudrate= 115200, timeout=.1)

def write_read(x):
    Arduino.write(bytes(x,'utf-8'))
    time.sleep(0.05)
    data = Arduino.readline()
    return data

while True:
    num = input("Enter a number: ")
    value = write_read(num)
    print(value)
