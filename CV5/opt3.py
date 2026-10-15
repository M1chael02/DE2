from machine import ADC
import time

def read_ADC(adc, samples):
    # adc = ADC(26)
    raw = 0
    
    for _ in range(samples):
        raw = raw + adc.read_u16()

    raw_avg = round(raw / samples)
    voltage = 3.3 * raw_avg / 65_535

    return raw_avg, voltage

def main():
    adc = ADC(28)
    print("Turn the potentiometer; press Ctrl+C to stop.")

    try:
        while True:
            raw, voltage = read_ADC(adc, 25)

            print(
                f"raw: {raw:5d}\tvoltage: {voltage:.3f} V" 
            )
            time.sleep_ms(100)

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")


if __name__ == "__main__":
    main()