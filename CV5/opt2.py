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
    led_R = PWMLed(12)
    led_G = PWMLed(13)
    led_B = PWMLed(14)
    led_B_enabled = True

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
                led_B_enabled = not led_B_enabled
                if not led_B_enabled:
                    led_B.duty_u16(0)

            if sample_due:
                sample_due = False
                raw_x, voltage_x = read_adc(adc_x)
                raw_y, voltage_y = read_adc(adc_y)

                if led_B_enabled:
                    led_B.set_brightness(100)

                brightness_R = round(raw_x * 100 / 65535)
                led_R.set_brightness(brightness_R)

                brightness_G = round(raw_y * 100 / 65535)
                led_G.set_brightness(brightness_G)

                print(
                    f"\rX: {raw_x:5d} (brightness: {brightness_R} %)\t" 
                    f"Y: {raw_y:5d} (brightness: {brightness_G} %)\t"
                    f"Blue: {'on' if led_B_enabled else 'off'} ", end=""
                )

            time.sleep_ms(5)

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")

    finally:
        timer.deinit()
        led_R.duty_u16(0)
        led_G.duty_u16(0)
        led_B.duty_u16(0)
        time.sleep_ms(1)
        led_B.deinit()
        led_R.deinit()
        led_G.deinit()

if __name__ == "__main__":
    main()