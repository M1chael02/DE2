from machine import Pin
import time

def colour_switch():
    print("Press ctrl + c to stop")

    leds = [
            Pin("GP12", Pin.OUT),
            Pin("GP13", Pin.OUT),  # Use the correct GPIO pin for your LED
            Pin("GP14", Pin.OUT)   # Also Pin(3, Pin.OUT)
        ]

    try:
            while True:
                for led in leds:
                    led.value(1)
                    time.sleep(0.5)
                time.sleep(0.5)
    
                for led in leds:
                    led.value(0)
                    time.sleep(0.5)
                time.sleep(0.5)
    
                # Show activity without moving to the next line
                print(".", end="")

    except KeyboardInterrupt:
            print("\nProgram stopped. Exiting...")
            for led in leds:
                 led.value(0)

        
if __name__ == "__main__":
    colour_switch()