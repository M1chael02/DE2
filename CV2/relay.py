from machine import Pin
import time

def control_relay():
    relay = Pin(16, Pin.OUT)  # Use the correct GPIO pin for your relay module

    print("Press Ctrl+C to stop")

    try:
        while True:
            relay.value(1)
            print("Relay ON")
            time.sleep(0.2)

            # TODO: Turn the relay off
            relay.value(0)
            print("Relay OFF")
            time.sleep(0.2)

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")
        relay.value(0)


if __name__ == "__main__":
    control_relay()