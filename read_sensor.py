import requests 
from sense_hat import SenseHat
import smbus
import time

while True:
    try:
        pressure=0
	sense = SenseHat()
	pressure = sense.get_pressure()
        data = {'pressure':pressure}
	print(pressure)

        #send http request to sense serverless function with pressure
        #data

        r=requests.post('http://127.0.0.1:8080/function/sensor',data)
        print(r.text)
	sense=SenseHat()
	sense.show_message(r.text)
    except KeyboardInterrupt:
    	sys.exit()
