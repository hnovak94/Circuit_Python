import time
from digitalio import DigitalInOut, Direction
# importing DigitalInOut and Direction from the library
# makes the code simpler and quicker to write

class FancyLED:

    def __init__(self, pin1, pin2):
    # all actions will include these two pins
    # i only had 4 LEDS so each involves 2 LEDS
    # instead of 3

        self.p1 = DigitalInOut(pin1)
        self.p1.direction = Direction.OUTPUT

        self.p2 = DigitalInOut(pin2)
        self.p2.direction = Direction.OUTPUT

    def alternate(self):
        self.p1.value = True
        self.p2.value = False
        time.sleep(.7)
        self.p1.value = False
        self.p2.value = True
        time.sleep(.7)
        print("alternate")

    def blink(self):
        self.p1.value = True
        self.p2.value = True
        time.sleep(.5)
        self.p1.value = False
        self.p2.value = False
        time.sleep(.5)
        print("blink")

    def chase(self):
        self.p1.value = True
        self.p2.value = False
        time.sleep(.2)
        self.p1.value = True
        self.p2.value = True
        time.sleep(1)
        self.p1.value = False
        self.p2.value = True
        time.sleep(.2)
        self.p1.value = False
        self.p2.value = False
        time.sleep(1)
        print("chase")

    def sparkle(self):
        self.p1.value = True
        self.p2.value = False
        time.sleep(.1)
        self.p1.value = False
        self.p2.value = True
        time.sleep(.1)
        print("sparkle")

