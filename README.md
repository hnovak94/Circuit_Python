# Circuit Python

## LED Blink/Connecting to Github
[Code](https://github.com/hnovak94/Circuit_Python/blob/main/code/led_blink.py)
### Lessons

This assignment and began using CircuitPython for the first time. The assignment was to blink an led which required a new library: digitalio. In CircuitPython the LED is not "high" or "low" but "true" or "false". 

### Wiring

<img src = "https://github.com/hnovak94/Circuit_Python/blob/main/media%2Bwiring/led_blink_wd.png" height = "250">

## Servo with Capacitive Touch

[Code](https://github.com/hnovak94/Circuit_Python/blob/main/code/cp_servo.py)

### Lessons

This assignment I continued to learn how to use CircuitPython. The assignment was to code the capacitive touch ability with the metro express with a continuous servo. The library for capacitive touch is touchio, and the libraries required for the servo are pulseio and servo. The servo library had to be downloaded manually onto the metro express. The first major thing that I had problems with was that I was saving the code to a folder not onto the metro. The second thing was that I was not saving the code as main.py which meant it was working. 

### Wiring

<img src= "https://github.com/hnovak94/Circuit_Python/blob/main/media%2Bwiring/cp_servo_wd.png" height = "250">

## LCD with Capacitive Touch

[Code](https://github.com/hnovak94/Circuit_Python/blob/main/code/captouchlcd.py)

### Lessons

For this assignment I had to again use capacitive touch, but this time with an LCD screen. This assignment was the most challenging because of the libraries. I had to spend a lot of time wiping the metro express and readding the libraries. I was able to get them working using files updated by Dr. Shields. The code in itself was not that challenging, but it took a lot of time and trial and error to get the libraries working. I also kept having a problem that it wouldn't load my code due to a "soft reboot", which was solvable by merely ejecting the circuit python drive. 

### Wiring

<img src= "https://github.com/hnovak94/Circuit_Python/blob/main/media_wiring/captouchlcd_wd.png" height = "250">

#### *Note
The LCD screen used for the assignment used an LCD backpack which has only 4 pins. They go to GND, 5V, SCL, and SDA. 

## Photointerrupter

[Code](https://github.com/hnovak94/Circuit_Python/blob/main/code/photointerrupt_cp.py)

### Lessons

This assignment I had to get a photointerrupter working with circuitpython. I found helpful code online that was the baseline. I relied more on code that I found than with other assignments, so the biggest part was figuring out what the different parts of the code meant, so I could edit and comment it appropriately. One thing that I found out this assignment, which I can use in other assignments, is importing specific commands from the library, not just the whole library in itself. This makes the code much simpler and faster to write. Instead of continuously having to write "digitalio.etc" you can import from the digitalio library "DigitalInOut" or "Direction" which saves time. 

### Wiring Diagram

<img src= "https://github.com/hnovak94/Circuit_Python/blob/main/media_wiring/p.interrupt_wd.png" height = "250">

## Distance Sensor

[Code](https://github.com/hnovak94/Circuit_Python/blob/main/media_wiring/hcsr04.py)

### Lessons

For this assignment we had to code the neopixel light on the metro express with the ultrasonic sensor. A big problem I had was finding any website that had information about doing color gradients with the neopixel. I broke the rainbow into steps that I could understand, but there was still some math that took me awhile to figure out. I had to do research online and look at peer work. The starter code I used was from the adafruit website [here](https://learn.adafruit.com/ultrasonic-sonar-distance-sensors/python-circuitpython), which gives both wiring diagrams and a starter code.  

### Wiring
<img src= "https://github.com/hnovak94/Circuit_Python/blob/main/code/hcsr04_wd.png" height = "250">

## Classes, Objects, + Modules

[Class](https://github.com/hnovak94/Circuit_Python/blob/main/code/rgb_class/RGB.py)

[Main](https://github.com/hnovak94/Circuit_Python/blob/main/code/rgb_class/rgb_main.py)

### Lessons
For this assignment I had to figure out how to code the annode RGB LEDs. At first when I did research the adafruit website said they had to be coded using PMW pins (the pulseio library), but I couldn't get that code to work, so I tried just using the digitalio library which worked. I didn't quite understand the logic of the instances at first, so it was useful to match up the logic that I understood of the RGB led with the sample dog code used in the assignment. 

### Wiring
<img src= "https://github.com/hnovak94/Circuit_Python/blob/main/media_wiring/rgb_class_wd.png" height = "250">

## Fancy LED
[Class](https://github.com/hnovak94/Circuit_Python/blob/main/code/fancyLED.py)

[Main](https://github.com/hnovak94/Circuit_Python/blob/main/code/fancyLED_main.py)

### Lessons

For this assignment I had to create a FancyLED class so that LEDs would do different things. My first problem was that I didn't have enough LEDs, so although the assignment calls for 6 LEDs, I did it with 4. I was also still kind of confused about classes and objects (although this assignment was still like the RGB assignment), so I did some extra research. [This](https://www.youtube.com/watch?v=8yjkWGRlUmY) video was helpful. My biggest problems after that were with formatting, which I still don't totally understand, but I figured it out through trial and error. As with previous assignments, comparing the logic of what I was doing with the LEDs to the previous assignment with the RGB LEDs was very helpful.

### Wiring

<img src= "https://github.com/hnovak94/Circuit_Python/blob/main/media_wiring/fancyLED_wd.png" width = "250">
 
