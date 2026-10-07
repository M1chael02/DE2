from machine import Pin
import time


class Button:
    """Read an active-low button with an internal pull-up resistor."""

    def __init__(self, pin_number):
        self.pin = Pin(pin_number, Pin.IN, Pin.PULL_UP)
        self._raw_value = self.pin.value()
        self._stable_value = self._raw_value
        self._last_change = time.ticks_ms()

    def is_pressed(self):
        """Return True while the button is pressed."""
        return not self.pin.value()

    def is_released(self):
        """Return True while the button is released."""
        # TODO: Complete this method.
        if self.pin.value() == 1:
            return True
        else:
            return False

    def read_button_state(self):
        """Return 'pressed' or 'released'."""
        # TODO: Complete this method.
        if self.is_released() == True:
            return "released"
        else:
            return "pressed"

    def was_pressed(self, debounce_ms=20):
        """Return True once when a stable press is detected."""
        raw_value = self.pin.value()
        if raw_value != self._raw_value:
            self._raw_value = raw_value
            self._last_change = time.ticks_ms()

        elapsed = time.ticks_diff(time.ticks_ms(), self._last_change)
        if elapsed >= debounce_ms and raw_value != self._stable_value:
            self._stable_value = raw_value
            return raw_value == 0

        return False


if __name__ == "__main__":
    button = Button(17)

    # while True:
    #     if button.was_pressed():
    #         print("Button pressed")
    #     time.sleep_ms(1)
    
    # while True:
    #     if button.is_pressed():
    #         print("Button pressed")
    #     time.sleep_ms(1)

    # while True:
    #     if button.is_released():
    #         print("Button released")
    #     time.sleep_ms(1)

    # while True:
    #     print(f"Button state: {button.read_button_state()}")
    #     time.sleep_ms(50)