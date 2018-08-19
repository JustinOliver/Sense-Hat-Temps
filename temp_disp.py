#!/usr/bin/env python3

# temp_disp.py - print out the temp stuff

from sense_hat import SenseHat
from time import sleep, strftime
from tkey import tnumber, sid, key, mynumber
import textmyself

sense = SenseHat()
sense.clear()


temp = sense.get_temperature() * 9/5 + 32
hum = sense.get_temperature_from_humidity() * 9/5 + 32
pre = sense.get_temperature_from_pressure() * 9/5 + 32
print("The three temps are {}, {}, {}" .format(temp, hum, pre))
print('')
sense.clear()
humidity = sense.get_humidity() 
print("The humidity is {}" .format(humidity))
print('')
sense.clear()
pressure = sense.get_pressure()
print("The pressure is {}" .format(pressure))

# Output results to a txt file to reference later

time = strftime("%c")
stuff = open('temps.txt', 'a')
stuff.write('Time and date at recording: {}\r\n' .format(time))
stuff.write('	Tempeture readings are: {}, {}, {} \r\n' .format(temp, hum, pre))
stuff.write('	Humidity is: {} \r\n' .format(humidity))
stuff.write('	Pressure is: {} \r\n' .format(pressure))
stuff.write('\r\n \r\n')
#stuff.write('Date and time of record: \n' + time + '\n')
stuff.close()

textmyself.textmyself('The current temp in your apartment is {:.1f}, humidity is {:.3f}, pressure is {:.4f}' .format(temp, humidity, pressure))