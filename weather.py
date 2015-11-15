import requests,json

def kelvin_to_celcius(temp):
    return round(temp-273.15,0)

def city_weather(city):
    return json.loads(requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'?id=524901&APPID=51327d8e2acca3b85af86a5c7ac69785').text)


city_name = str(input("Podaj miasto\n"))




print ("Temperatura dla miasta "+city_name+" wynosi "+ str(kelvin_to_celcius(city_weather(city_name)["main"]["temp"]))+" "+ u'\N{DEGREE CELSIUS}')