import RPi.GPIO as GPIO
import dht11 #libreria importada
import requests
#api interna
API_ENDPOINT = "http://192.168.1.18:8000/api/temps"

# incia GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# leer valores del pin 20
instance = dht11.DHT11(pin=20)

temp_casa=""
hum_casa=""
try:

        result = instance.read()
        if result.is_valid():
            temp = {'tempId':1,'temp':result.temperature,"hum":result.humidity} #creamos un array con las varibles
            temp_casa = "%-3.1f" % result.temperature #añadimos temperatura al array
            hum_casa= "%-3.1f" % result.humidity #añadimos humedad al array
            x = requests.post(API_ENDPOINT, temp) #realiza el POST

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()

print(temp) #imprime temperatura en pantalla
