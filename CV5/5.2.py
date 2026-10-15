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
    adc_x = ADC(26)
    adc_y = ADC(27)
    
    
    print("Turn the potentiometer; press Ctrl+C to stop.")

    try:
        while True:
            raw_x, voltage_x = read_ADC(adc_x, 10)
            raw_y, voltage_y = read_ADC(adc_y, 10)

            print(
                f"raw_x: {raw_x:5d}\tvoltage_x: {voltage_x:.3f} V\n"
                f"raw_y: {raw_y:5d}\tvoltage_y: {voltage_y:.3f} V\n" 
            )
            time.sleep_ms(100)

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")


if __name__ == "__main__":
    main()