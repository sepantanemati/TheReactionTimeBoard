import machine
import time
import random
from machine import Pin, SoftI2C
from machine import Pin, SoftI2C
import ssd1306
import time
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
print(i2c.scan())

start = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
player1 = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
player2 = machine.Pin(23, machine.Pin.IN, machine.Pin.PULL_UP)
lamp1 = machine.Pin(5, machine.Pin.OUT)
lamp2 = machine.Pin(16, machine.Pin.OUT)
lamp3 = machine.Pin(17, machine.Pin.OUT)
greenlamp = machine.Pin(18, machine.Pin.OUT)

print("ready")

while True:
    if start.value() == 0:
        print("starting")
        time.sleep(3)
        
        wait = random.randint(1, 3)
        lamp1.value(1)
        time.sleep(2)
        oled.fill(0)
        oled.text("3...", 0, 0)
        oled.show()
        time.sleep(wait)
        lamp1.value(0)
        
        wait = random.randint(1, 3)
        lamp2.value(1)
        oled.fill(0)
        oled.text("2...", 0, 0)
        oled.show()
        time.sleep(wait)
        lamp2.value(0)
        
        wait = random.randint(1, 3)
        lamp3.value(1)
        oled.fill(0)
        oled.text("1...", 0, 0)
        oled.show()
        time.sleep(wait)
        lamp3.value(0)
        
        greenlamp.value(1)
        oled.fill(0)
        oled.text("GO!", 0, 0)
        oled.show()
        starttime = time.ticks_ms()
        winner = None
        endtime = 0
        
        while winner is None:
            if player1.value() == 0:
                endtime = time.ticks_ms()
                winner = "Player 1"
            elif player2.value() == 0:
                endtime = time.ticks_ms()
                winner = "Player 2"
            time.sleep(0.001)
            
        timetaken = time.ticks_diff(endtime, starttime)
        secs = timetaken / 1000
        print(f"{winner} won the reaction time was {secs:.2f} seconds")
        greenlamp.value(0)
        oled.fill(0)
        oled.text(f"{winner} won,", 0, 0)
        oled.text(f"reaction time", 0, 16)
        oled.text(f"was {secs:.2f} seconds", 0, 32)
        oled.show()
        
        time.sleep(2)
        
    time.sleep(0.1)
    
