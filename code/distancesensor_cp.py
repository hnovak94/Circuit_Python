import time
import board
import adafruit_hcsr04
import neopixel
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    try:
        print((sonar.distance))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
    dot.fill((10, 0, 0))
    time.sleep(.5)
