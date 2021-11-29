import serial
import time
import numpy as np

Arduino = serial.Serial(port="/dev/ttyUSB0", baudrate=115200, timeout=.1)


def write_read(x):
    Arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    #data = Arduino.readline()
    #return data


def inverse_kinematics(x, y, L1, L2):
    theta2 = np.arccos((np.sqrt(x) + np.sqrt(y) - np.sqrt(L1)) / (2*L1*L2))
    if x < 0 and y < 0:
        theta2 = -theta2

    theta1 = np.arctan(x / y) - np.arctan((L2*np.sin(theta2)) / (L1+L2*np.cos(theta2)))
    theta2 = -theta2 * 180/np.pi
    theta1 = theta1 * 180/np.pi

    if x >= 0 and y >= 0:
        theta1 = 90-theta1
    if x < 0 and y > 0:
        theta1 = 90 - theta1
    if x < 0 and y < 0:
        theta1 = 270 - theta1
        phi = 270 - theta1 - theta2
        phi = -phi
    if x > 0 and y < 0:
        theta1 = -90 - theta1
    if x < 0 and y == 0:
        theta1 = 270 + theta1

    phi = 90 + theta1 + theta2
    phi = - phi

    if np.abs(phi) > 165:
        phi = 180 + phi

    return theta1, theta2, phi


x = 1
y = 1
z = 1
while z < 15:

    # data :
    # data[0] - SAVE button status
    # data[1] - RUN button status
    # data[2] - Joint 1 angle
    # data[3] - Joint 2 angle
    # data[4] - Joint 3 angle
    # data[5] - Z position
    # data[6] - Speed value
    # data[7] - Acceleration value
    L1 = 228
    L2 = 136.5
    x = float(input("x: "))
    y = float(input("y: "))
    z = float(input("z: "))
    save = input("Save: ")
    run = input("run: ")
    theta1, theta2, phi = inverse_kinematics(x, y, L1, L2)
    theta1 = str(round(theta1, 2))
    theta2 = str(round(theta2, 2))
    phi = str(round(phi, 2))
    mes = str(save) + "," + run + "," + theta1 + "," + theta2 + "," + phi + "," + str(z) + "," + str(500) + "," + str(50)
    write_read(mes)
    print(theta1, theta2, phi)
