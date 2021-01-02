import board
import adafruit_hcsr04

import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:

    distance = sonar.distance

    try:
        print((distance))

        step = 7.5
        # there are 4 basic changes in color
        # the range from 5 to 35 is 30
        # 35 divided by 4 is 7.5
        # so the step between is 7.5

        red = 0
        green = 0
        blue = 0
        # these values are like the dotfill
        # from the first assignment
        # (red, green, blue) : (0, 0, 0)

        if distance < 12.5:
            # 5 + 7.5 = 12.5
            # i attempted to do
            # 5 < distance < 12.5 but it didn't work
            # so i tried doing just 12.5

            red = 255
            green = 0
            blue = max(0,
                       int(((distance - 5) / step) * 255)
                       )

            # rgb value cannot be negative
            # so the maximum must be set at 0
            # so it doesn't go below

        if 12.5 < distance < 20:
            # magenta to blue
            # 12.5 + 7.5 = 20

            red = 255 - int(((distance - 12.5) / step) * 255)
            green = 0
            blue = 255

            # subtract from highgest point
            # so the color number stays between
            # 0 and 255

        if 20 < distance < 27.5:
            # blue to cyan
            # 20 + 7.5 = 27.5

            red = 0
            green = int(((distance - 20) / step) * 255)
            blue = 255

        if distance > 27.5:
            # cyan to green
            # anything higher than 35
            # is green

            red = 0
            green = 255
            blue = max(0,
                       255 - int(((distance - 27.5) / step) * 255)
                       )
            # again setting max so it goes
            # no higher than 255
        dot.fill((red, green, blue))

    except RuntimeError:
        print("Retrying")

    time.sleep(0.5)
