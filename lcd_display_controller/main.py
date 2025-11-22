from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd
_init()
 
DEFAULT_I2C_ADDR = 0x3F # Или 0x27 в зависимости от твоей платы IoT
 
 
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
lcd.backlight_on()
lcd.putstr("Hello, World!\nSecond Line")