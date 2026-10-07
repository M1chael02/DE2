from machine import Pin
import time


class Led(Pin):  # Led is a subclass of Pin
    """A class to control an LED connected to a specific GPIO pin."""

    def __init__(self, pin_number):
        """Initialize the LED on a specific GPIO pin."""
        super().__init__(pin_number, Pin.OUT)

    def toggle(self):
        """Toggle the LED state."""
        self.value(not self.value())


if __name__ == "__main__":
    led = Led(2)

    print("\nTurning LED on and off...")
    # TODO: Test Led's methods