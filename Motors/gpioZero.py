from gpiozero import OutputDevice

a = OutputDevice(26)
b = OutputDevice(20)
while True:
    a.on()
