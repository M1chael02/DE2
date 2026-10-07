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

    def on(self):
        """Power the LED on"""
        self.value(1)

    def off(self):
        """Power the LED on"""
        self.value(0)

    def pulse(self, duration=0.25):
        """Blink the LED one time."""
        self.value(1)
        time.sleep(duration)
        self.value(0)

    def blink(self, duration=0.5, times=2):
        """Blink the LED a number of times."""
        # TODO: Complete the method
        for x in range(times):
            self.value(1)
            time.sleep(duration)
            self.value(0)
            time.sleep(duration)    


if __name__ == "__main__":
    led = Led(2)
    led2 = Led(3)

    #print("\nTurning LED on and off...")
    # TODO: Test Led's methods

    #led.pulse()
    #led2.blink(0.5, 3)

    # try:
    #     counter = 2
    #     while True:
    #         print(f"Counter: {counter}")
    #         onFor = 1/counter
    #         wait = 1 - 2 * onFor
    #         print(f"Speed of blink: {onFor}")
    #         led.blink(onFor, 2)
    #         print(f"Waiting for: {wait}")
    #         time.sleep(wait)
    #         counter += 1
    #         print(f"Counter: {counter}")

    # except KeyboardInterrupt:
    #     print("\nProgram stopped. Exiting...")

    print(f"isinstance(led, Led): {isinstance(led, Led)}")
    print(f"isinstance(led, Led): {isinstance(led, Pin)}\n") 

    print(f"issubclass(Led, Pin): {issubclass(Led, Pin)}")
    print(f"issubclass(Pin, Led): {issubclass(Pin, Led)}")