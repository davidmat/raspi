from sense_hat import SenseHat

sense = SenseHat()
temp = sense.get_temperature()
temphum = sense.get_temperature_from_humidity()
temppres = sense.get_temperature_from_pressure()

print(temppres)