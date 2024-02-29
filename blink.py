from machine import Pin
from utime import sleep

led = Pin("LED", Pin.OUT)

print("Led is flashing")

while True:
    try:
        led.toggle()
        sleep(1)
    except KeyboardInterrupt:
        break

led.off()
print("Finished")