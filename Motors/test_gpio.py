from gpiozero import OutputDevice
from time import sleep

for val_a in range(1, 28):
    a = OutputDevice(val_a)
    val_b = 20
    #for val_b in range(1, 28):
    if val_a != val_b:
        b = OutputDevice(val_b)
        a.on()
        print(val_a, val_b)
        sleep(1)

