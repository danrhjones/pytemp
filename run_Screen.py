import RGB
import time
import math
import requests

colorR = 64
colorG = 128
colorB = 64

lcd=RGB.RGB1602(16,2)

t=0
while True:

    r = int((abs(math.sin(3.14*t/180)))*255)
    g = int((abs(math.sin(3.14*(t+60)/180)))*255)
    b = int((abs(math.sin(3.14*(t+120)/180)))*255)
    t = t + 3

    response = requests.get("http://127.0.0.1:8000/monitor")
    output = response.json()

    lcd.setRGB(r,g,b)
    lcd.setCursor(0, 0)
    lcd.printout("the temp is {}c".format(output["temp"]))
    lcd.setCursor(0, 1)
    lcd.printout("humidty is {}%".format(output["humidity"]))
    time.sleep(0.3)
