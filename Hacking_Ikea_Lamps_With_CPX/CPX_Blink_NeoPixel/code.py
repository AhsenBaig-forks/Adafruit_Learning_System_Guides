import time

from adafruit_circuitplayground.express import cpx

while True:
    cpx.pixels[0] = (abs(cpx.pixels[0][0] - 255), 0, 0)
    time.sleep(0.5)
