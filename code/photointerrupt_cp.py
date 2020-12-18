
from digitalio import DigitalInOut, Direction, Pull  
#  importing the above makes the code faster to write
import time
import board

interrupter = DigitalInOut(board.D7)  # interrupter pin at digital pin 7
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP  # input pin made high when reading nothing

counter = 0  # no. of interrupts at 0

photo = False
state = False

max = 4  # check no. of interrupts every 4 seconds
start = time.time()

while True:
    photo = interrupter.value  # variable photo = value (high or low)
    if photo and not state:  # if it has been interruped
            counter += 1  # record interrupt
    state = photo

    remaining = max - time.time()  # time left is equal to 4 secs minus time passed

    if remaining <= 0: #  if time is up
        print("Number of Interrupts:", str(counter))  # print no. of interrupts + counter
        max = time.time() + 4  # start timer over
        counter = 0  # return no. of interrupts to 0

