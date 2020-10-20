import board
import time
import digitalio # helps to control digital output

led = digitalio.DigitalInOut(board.A1) # sets A1 as pin

led.direction = digitalio.Direction.OUTPUT # makes pinmode output

while True:

    led.value = True # led is ON
    time.sleep(.5)
    led.value = False # led is OFF
    time.sleep(.5)






