from machine import Pin
import time


class RGBLed:
    """Control a common-cathode RGB LED using three GPIO pins."""

    def __init__(self, red_pin, green_pin, blue_pin):
        self.red_pin = Pin(red_pin, Pin.OUT)
        self.green_pin = Pin(green_pin, Pin.OUT)
        self.blue_pin = Pin(blue_pin, Pin.OUT)
        self.off()

    def set_color(self, red, green, blue):
        """Set each color channel to 0 (off) or 1 (on)."""
        self.red_pin.value(red)
        # TODO: Set the value of each output pin.
        self.green_pin.value(green)
        self.blue_pin.value(blue)

    def off(self):
        """Turn all color channels off."""
        # TODO: Use set_color() to turn all channels off.
        self.red_pin.value(0)
        self.green_pin.value(0)
        self.blue_pin.value(0)

    def red(self):
        """Display red."""
        self.set_color(1, 0, 0)

    def white(self):
        """Turn on all three color channels."""
        self.set_color(1, 1, 1)


if __name__ == "__main__":
    rgb = RGBLed(12, 13, 14)

    """rgb.red()
    time.sleep(1)

    rgb.off()
    time.sleep(1)

    rgb.set_color(0, 0, 1)
    time.sleep(1)

    rgb.off()
    time.sleep(1)

    rgb.white()
    time.sleep(1)

    rgb.off()"""

    rgb = RGBLed(12, 13, 14)

    #cyan   
    rgb.set_color(0, 1, 1)
    time.sleep(1)

    rgb.off()
    time.sleep(1)

    #magenta
    rgb.set_color(1, 0, 1)
    time.sleep(1)

    rgb.off()
    time.sleep(1)

    #yellow
    rgb.set_color(1, 1, 0)
    time.sleep(1)

    rgb.off()
    time.sleep(1)
