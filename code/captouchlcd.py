import board
import touchio
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# some LCDs are 0x3f... some are 0x27, import all libraries for lcd
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)
state = True
yellow = touchio.TouchIn(board.A3)  # establishes yellow wire at A3
blue = touchio.TouchIn(board.A4)  # establishes blue wire at A4
lcd.set_cursor_pos(0, 0)  # starting position is first row of lcd
time.sleep(2)
counter = 0  # counter starts at zero

print("running")
while True:

    if blue.value:  #  blue wire toggles counter direction
        message = "GOING UP  "  #  prints direction
        state = False

    else:
        message = "GOING DOWN "  #  prints direction
        state = True

    lcd.set_cursor_pos(0, 0) #  first row of lcd screen
    lcd.print(message)  # print direction "up or down"
    if state is True:  # if direction is down
        direction = -1  # subtract 1 from counter
    else:  # if direction is up
        direction = 1  # add 1 to counter

    if yellow.value:
        counter = counter + direction  # controls which way it counts
        lcd.set_cursor_pos(1, 0)  # second line of lcd screen
        message = "PRESS NO. "
        message += str(counter)  # print counter number to lcd
        print(counter)  # prints counter to serial moniter
        lcd.print(message)  # prints press no + counter

    while yellow.value:   # so it doesn't count continuously
        time.sleep(.25)

    else:
        counter = counter  # if not touched, counter remains the same
