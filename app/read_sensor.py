import serial
import time

import config
from send_email import send_email
 
arduino = serial.Serial(config.ARDUINO_SERIAL_PORT, 9600)
time.sleep(2)  # wait for 2 secounds for the communication to get established

arduino.flushInput()

send_email_flag = True

while True:
    try:
        ser_bytes = arduino.readline()
        decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
        sensor_1, sensor_2 = decoded_bytes.split(';')
        #print('{} '.format(sensor_1))
        if float(sensor_1) > 0 and send_email_flag:
            send_email()
            send_email_flag = False

        if float(sensor_1) == 0:
            send_email_flag = True
    except:
        print("Keyboard Interrupt")
        break

