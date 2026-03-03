import requests
from colorama import init, Fore

init(autoreset=True)

API_KEY = "75f2a1682081a98824409849dceb5ec8"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=75f2a1682081a98824409849dceb5ec8&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            print(Fore.CYAN + "\nWeather Details")
            print(Fore.CYAN + "------------------------")
            print(Fore.YELLOW + f"City: {city}")
            print(Fore.GREEN + f"Temperature: {data['main']['temp']}°C")
            print(Fore.BLUE + f"Humidity: {data['main']['humidity']}%")
            print(Fore.MAGENTA + f"Condition: {data['weather'][0]['description']}")
            print(Fore.WHITE + f"Wind Speed: {data['wind']['speed']} m/s")
        else:
            print(Fore.RED + f"Error: {data.get('message')}")

    except Exception as e:
        print(Fore.RED + f"Something went wrong: {e}")


if __name__ == "__main__":
    while True:
        city = input(Fore.CYAN + "\nEnter city name (or type 'exit'): ")
        if city.lower() == "exit":
            print(Fore.GREEN + "Exiting Weather App 🌦️")
            break
        get_weather(city)








    