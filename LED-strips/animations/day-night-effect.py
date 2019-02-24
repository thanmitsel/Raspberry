#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from neopixel import *
import argparse

# LED strip configuration:
LED_COUNT      = 30      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53



# Define functions which animate LEDs in various ways.
def light_more_than_one(strip, idx, pad, color):
    """Light a subset (window) of the led strips"""
    for led in range(idx-pad, idx+pad+1):
        strip.setPixelColor(led, color)
    strip.show()

def select_color(rgb_start, rgb_end, pad, LED_count):
    """Outputs a list with all range of colors of rgb"""
    rgb_list = []
    for color in range(len(rgb_start)):
       diff = rgb_end[color] - rgb_start[color]
       step = diff/LED_count
       rgb_list.append([i*step+rgb_start[color] for i in range(LED_count)])
    return rgb_list

def dayNight(strip, pad=1, sec=0.05):
    """Rolling Window from one color to another and backwards"""
    RGB_before = [255, 255, 0] # Yellow
    RGB_after = [255, 255, 255] # White
    rgb_list = select_color(RGB_before, RGB_after, pad, strip.numPixels())
    two_way_count = [range(pad, strip.numPixels()-pad), range(strip.numPixels()-pad-1, 0+pad-1, -1)]
    for way in two_way_count:
        for i in way:
            light_more_than_one(strip, i, pad, Color(rgb_list[0][i], rgb_list[1][i], rgb_list[2][i])) # Turn on
            time.sleep(sec)
            light_more_than_one(strip, i, pad, Color(0, 0, 0)) # Turn off

def multi_wipe(strip, sec=0.05):
    RGB_before = [255, 255, 0] # Yellow
    RGB_after = [255, 255, 255] # White
    rgb_list = select_color(RGB_before, RGB_after, 0, strip.numPixels()) 
    range_list = [range(strip.numPixels()), range(strip.numPixels()), range(strip.numPixels()-1, 0-1, -1), range(strip.numPixels()-1, 0-1, -1)]
    for count, way in enumerate(range_list):
        for i in way:
            if (count+1)%2!=0:
                strip.setPixelColor(i, Color(rgb_list[0][i], rgb_list[1][i], rgb_list[2][i]))
            else:
                 strip.setPixelColor(i,Color(0, 0, 0))
            strip.show()
            time.sleep(sec)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            print ('Day-Light animations.')
            dayNight(strip)  # Window wipe
            print('Multiple wipe animation')
            multi_wipe(strip) # Multiple wipe

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)
