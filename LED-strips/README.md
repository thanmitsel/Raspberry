# Controlling Addresable LED with Raspberry PI

## Hardware

### Required Hardware
* Addressable LED Strip 
	* Chip LED: RGB WS2812
	* Count of LED: 30
	* Size: 1m
* 2 phone chargers
	* Current: 2A
	* Voltage: 5V DC
* Raspberry pi B+
* Breadboard
* Wires (Male to Female)
* Tools to strip wires

### Conecting Raspberry with LED strip
* Connect the 18th GPIO, which has PWM capabilies

## Software
### Required Software
* Raspbian


### Preparation
1. Update packages
> sudo apt-get update upgrade

2. Install required packages
> sudo apt-get install gcc make build-essential python-dev git scons swig

3. Install support for WS2812
> curl -L http://coreelec.io/33 | bash

4. Move to the directory with example scripts
> cd rpi_ws281x/python/examples/

5. Run a test script. 
> sudo python strandtest.py

6. If any problem occurs with libraries you can always search for the package with pip.
> pip3 search neopixel


*References*
1. https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips/
2. https://core-electronics.com.au/tutorials/ws2812-addressable-leds-raspberry-pi-quickstart-guide.html
