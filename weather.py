import requests, json

answer = "y"


def kelvin_to_celcius(temp):
    return round(temp - 273.15, 0)


def city_weather(city):
    return json.loads(requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=' + city + '?id=524901&APPID=51327d8e2acca3b85af86a5c7ac69785').text)


print("""Welcome to LOCAL WEATHER program!
         Choose one of the following options:
         1. Weather for Wrocław
         2. Weather for Świdnica
         3. Weather for Oława
         4. Weather for Trzebnica
         5. Weather for Brzeg""")

while (answer == "y" or answer == "Y"):
    choice = input("Your choice is: ")
    if choice == "1":
        print("Temperature for Wrocław is " + str(
            kelvin_to_celcius(city_weather("Wroclaw")["main"]["temp"])) + " " + u'\N{DEGREE CELSIUS}')
    elif choice == "2":
        print("Temperature for Swidnica is " + str(
            kelvin_to_celcius(city_weather("Swidnica")["main"]["temp"])) + " " + u'\N{DEGREE CELSIUS}')
    elif choice == "3":
        print("Temperature for Olawa is " + str(
            kelvin_to_celcius(city_weather("Olawa")["main"]["temp"])) + " " + u'\N{DEGREE CELSIUS}')
    elif choice == "4":
        print("Temperature for Trzebnica is " + str(
            kelvin_to_celcius(city_weather("Trzebnica")["main"]["temp"])) + " " + u'\N{DEGREE CELSIUS}')
    elif choice == "5":
        print("Temperature for Brzeg is " + str(
            kelvin_to_celcius(city_weather("Brzeg")["main"]["temp"])) + " " + u'\N{DEGREE CELSIUS}')
    elif choice == "6":
        city_name = str(input("Podaj miasto\n"))
        print("Temperature for " + city_name + " is " + str(
            kelvin_to_celcius(city_weather(city_name)["main"]["temp"])) + " " + u'\N{DEGREE CELSIUS}')
    else:
        print("Wrong choice, try again ? Y/N")
    answer = input("Would you like to check the weather for different region?\n")
print("Thanks for using our LOCAL WEATHER program!")
