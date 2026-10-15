from gpio_devices import Button, PWMLed
from machine import ADC, Timer
import time

sample_due = False


def timer_handler(timer):
    global sample_due

    sample_due = True


def read_adc(adc, samples=8):
    total = 0
    for _ in range(samples):
        total += adc.read_u16()

    average = round(total / samples)
    voltage = average * 3.3 / 65_535
    return average, voltage


def main():
    global sample_due

    adc_x = ADC(26)
    adc_y = ADC(27)
    button = Button(17)
    led = PWMLed(2)
    led2 = PWMLed(3)
    led_enabled = True
    led2_enabled = True

    timer = Timer(-1)
    timer.init(
        period=100,
        mode=Timer.PERIODIC,
        callback=timer_handler
    )

    print("Move the joystick; press its button to toggle LED control.")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            if button.was_pressed():
                led_enabled = not led_enabled
                led2_enabled = not led2_enabled
                if not led_enabled:
                    led.duty_u16(0)
                    led2.duty_u16(0)

            if sample_due:
                sample_due = False
                raw_x, voltage_x = read_adc(adc_x)
                raw_y, voltage_y = read_adc(adc_y)

                if led_enabled:
                    brightness = round(raw_x * 100 / 65535)
                    led.set_brightness(brightness)
                    brightness2 = round(raw_y * 100 / 65535)
                    led2.set_brightness(brightness2)

                print(
                    f"\rX: {raw_x:5d} ({voltage_x:.2f} V)  "
                    f"Y: {raw_y:5d} ({voltage_y:.2f} V)  "
                    f"LED control: {'on' if led_enabled else 'off'} ", end=""
                )

            time.sleep_ms(5)

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")
    finally:
        timer.deinit()
        led.duty_u16(0)
        led.deinit()
        led2.duty_u16(0)
        led2.deinit()


if __name__ == "__main__":
    main()