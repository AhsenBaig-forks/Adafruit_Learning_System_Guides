import analogio
import board
import neopixel

# Initialize input/output pins
sensor_pin = board.A1  # input pin for the potentiometer
sensor = analogio.AnalogIn(sensor_pin)

pix_pin = board.D1  # pin where NeoPixels are connected
num_pix = 8  # number of neopixels
strip = neopixel.NeoPixel(pix_pin, num_pix, brightness=.15, auto_write=False)

color_value = 0
sensor_value = 0


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0) or (pos > 255):
        return 0, 0, 0
    if pos < 85:
        return int(pos * 3), int(255 - (pos * 3)), 0
    elif pos < 170:
        pos -= 85
        return int(255 - pos * 3), 0, int(pos * 3)

    pos -= 170
    return 0, int(pos * 3), int(255 - pos * 3)


def remap_range(value, left_min, left_max, right_min, right_max):
    # this remaps a value from original (left) range to new (right) range
    # Figure out how 'wide' each range is
    left_span = left_max - left_min
    right_span = right_max - right_min

    # Convert the left range into a 0-1 range (int)
    valueScaled = int(value - left_min) / int(left_span)

    # Convert the 0-1 range into a value in the right range.
    return int(right_min + (valueScaled * right_span))


# Loop forever...
while True:

    # remap the potentiometer analog sensor values from 0-65535 to RGB 0-255
    color_value = remap_range(sensor.value, 0, 65535, 0, 255)

    for i in range(len(strip)):
        strip[i] = wheel(color_value)
    strip.write()
