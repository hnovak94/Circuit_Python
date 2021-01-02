from fancyLED import FancyLED
import board

fancy1 = FancyLED(board.D1, board.D2)
fancy2 = FancyLED(board.D3, board.D4)

while True:
    fancy1.alternate()
    # first set of LEDS will alternate
    fancy2.blink()
    # second set of LEDS will blink
    fancy1.chase()
    # first set of LEDS will "chase"
    fancy2.sparkle()
    # second set of LEDS will "sparkle"
