from machine import Pin
import time


def button_control_led():
    led = Pin("LED", Pin.OUT)
    button = Pin(17, Pin.IN, Pin.PULL_UP)  # Use the correct GPIO pin for your button

    button_pressed = 0

    print("Press the button to toggle the LED. Press Ctrl+C to stop")

    try:
        while True:
            # The button is active LOW: pressed -> value() == 0
            if button.value() == 0:
                button_pressed +=1
                print("Button pressed")

                # Wait for button release and prevent multiple toggles from one press
                while button.value() == 0:
                    pass

                #led.toggle() #For bistable operation of the led
                led.on()
                print(f"Current LED state: {led.value()}")
                time.sleep(1)
                led.off()
                print(f"Current switch position: {button.value()}")
                print(f"Current LED state: {led.value()}")

                # TODO: Print the LED state to REPL
                
                print(f"\nCurrent button presses: {button_pressed}\n")
                time.sleep(0.1)
            

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")
        print(f"Button was pressed {button_pressed} times")
        led.value(0)


if __name__ == "__main__":
    button_control_led()