import digitalio  # library for leds


class RGB:

    def __init__(self, redpin, greenpin, bluepin):

        self.red = digitalio.DigitalInOut(redpin)
        self.red.direction = digitalio.Direction.OUTPUT
        # pinmode for red leg output
        self.green = digitalio.DigitalInOut(greenpin)
        self.green.direction = digitalio.Direction.OUTPUT
        # pinmode for green leg output
        self.blue = digitalio.DigitalInOut(bluepin)
        self.blue.direction = digitalio.Direction.OUTPUT
        # pinmode for blue leg output

    def red(self):
        # red on; blue + green off
        self.red.value = False
        self.green.value = True
        self.blue.value = True

    def magenta(self):
        # red + blue on; green off
        self.red.value = False
        self.green.value = True
        self.blue.value = False

    def blue(self):
        # blue on; red + green off
        self.red.value = True
        self.green.value = True
        self.blue.value = False

    def cyan(self):
        # green + blue on; red off
        self.red.value = True
        self.green.value = False
        self.blue.value = False

    def green(self):
        # green on; blue + red off
        self.red.value = True
        self.green.value = False
        self.blue.value = True

    def yellow(self):
        # red + green on; blue off
        self.red.value = False
        self.green.value = False
        self.blue.value = True


