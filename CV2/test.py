from machine import Pin
import time


def blink_leds():
    print("Press Ctrl+C to stop")

    # Use a list of GPIO pins
    leds = [
        Pin("GP2", Pin.OUT),  # Use the correct GPIO pin for your LED
        Pin("GP3", Pin.OUT)   # Also Pin(3, Pin.OUT)
    ]

    try:
        while True:
            for led in leds:
                led.value(1)
            time.sleep(0.5)

            for led in leds:
                led.value(0)
            time.sleep(0.5)

            # Show activity without moving to the next line
            print(".", end="")

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")

        # TODO: Turn both LEDs off
        leds[0].value(0)
        leds[1].value(1)




if __name__ == "__main__":
    blink_leds()