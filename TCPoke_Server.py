'''
It took me four years to paint like Raphael,
but a lifetime to paint like a child.
-- Pablo Picasso
Taken from Pepijn de vos work

Edited by Tchaly Bethmaure
'''

import serial
import machine
import time
import usocket as socket

LED = 25
pinSC = 4
pinSI = 5
pinSO = 3

buffer = None

led, uart, SC, SI, SO = None, None, None, None, None

connected = False;

s = None

def setup():
    print("Initialisation \n");
    SC = Pin(pinSC, Pin.IN)
    SI = Pin(pinSI, Pin.IN)
    SO = Pin(pinSO, Pin.OUT)

    serial = Serial(0, 8000);

    led = Pin(LED, Pin.OUT);

    s = socket(AF_INET, SOCK_STREAM)

    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s.bind(addr)
    s.listen(1)
    print('listening on', addr)

    print("Intialisation DONE\n")

def loop():
    cl, addr = s.accept()
    print('client connected from', addr)
    while connected:
        in_data = 0
        response = serial.recv()
        led.value(1)
        cl.send(response)
        led.value(0)
        other_gb_response = cl.recv()
        if other_gb_response:
            led.value(1)
            serial.write(other_gb_response)
            print(in_data)
            print("\n")
        else:
            cl.close()
            break
        led.value(0)
setup()
loop()
