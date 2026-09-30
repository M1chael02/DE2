from machine import Pin
from machine import Timer
import time

led_R = Pin("GP12", Pin.OUT)
led_G = Pin("GP13", Pin.OUT)
led_B = Pin("GP14", Pin.OUT)

relay = Pin("GP16", Pin.OUT)
relay.value(0)

button = Pin(17, Pin.IN, Pin.PULL_UP)

sound_delay = 1

blink_timer = Timer()

def traffic_light():
    try:
        while True:
           time.sleep(0.2)
           blink_timer.init(mode=Timer.PERIODIC, period=500, callback=relay)
           time.sleep(3)
           blink_timer.deinit()
           blink_timer.init(mode=Timer.PERIODIC, period=500, callback=relay)
           time.sleep(3)

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")
        led_R.value(0)
        led_G.value(0)
        led_B.value(0)

def relay(timer):
    if relay.value() == 0:
        relay.value(1)
    else:
        relay.value(0)
    


if __name__ == "__main__":
    traffic_light()