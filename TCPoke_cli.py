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


    print('listening on', addr)

    print("Intialisation DONE\n")

def loop():
    _, _, host, path = url.split('/', 3)
    f = fopen("tcpoke.cfg")
    ip = f.readline()
    addr = socket.getaddrinfo(ip, 80)[0][-1]
    s.connect(addr)
    print("connected to "+addr)
    while True:
        # Receive from GB data then send them to host
        led.value(1)
        response = serial.recv()
        if response:
            led.value(0)

            s.send(response)

            # sending data received via the Internet to GB salve (me)
            data_from_master = s.recv()

            if data_from_master:
                led.value(1)
                serial.write(data_from_master)
                led.value(0)
            else:
                break
    s.close()
setup()
loop()
