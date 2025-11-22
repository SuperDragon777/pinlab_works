from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd

_init()

DEFAULT_I2C_ADDR = 0x3F

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
lcd.backlight_on()

print("Enter text for LCD display (Ctrl+C to exit):")
print("(Use \\n for new line)")

while True:
    user_text = input("> ")
    lcd.clear()
    lcd.putstr(user_text)
    print("Display output: " + user_text)