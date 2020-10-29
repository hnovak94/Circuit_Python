#  import time
import board
import pulseio
import servo
import touchio

touch_A3 = touchio.TouchIn(board.A3)  # capacitive touch on A3
touch_A4 = touchio.TouchIn(board.A4)  # capacitive touch on A4
pwm = pulseio.PWMOut(board.A2,  frequency=50)  # servo connected to A2

my_servo = servo.ContinuousServo(pwm)  # creates servo object

while True:

    if touch_A3.value:  # if wire on A3 is touched
        my_servo.throttle = 1.0  # servo moves forward
    else:  # if wire on A3 is not touched
        my_servo.throttle = 0.0  # servo does not move
    if touch_A4.value:  # if wire on A4 is touched
        my_servo.throttle = -1.0  # servo moves in reversed
    else:  # if wire on A4 is not touched
        my_servo.throttle = 0.0  # servo does not move



