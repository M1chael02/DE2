from machine import Pin
from machine import lightsleep
import time


def main():
    """Main application entry point."""
    print("Press Ctrl+C to stop")

    # TODO 1: Initialize the on-board LED as an output pin
    # Hint: Use Pin("LED", Pin.OUT)
    led = Pin("LED", Pin.OUT)

    try:
        while True:
            # TODO 2: Toggle the LED state (or set it to high then low)
            led.on()
            lightsleep(500)
            led.off()
            lightsleep(500)
            # TODO 3: Add a delay so the blinking is visible (e.g., 500 ms)

    except KeyboardInterrupt:
        # This part runs when Ctrl+C is pressed
        led.off()
        print("\nProgram stopped. Exiting...")

        # Optional cleanup code
        # TODO 4: Ensure the LED is turned OFF before exiting


# Run this only when executed directly, not when imported
if __name__ == "__main__":
    main()