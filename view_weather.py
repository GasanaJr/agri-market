import requests
# pylint: disable=import-error


def viewWeather():
    print("Welcome To Live data section")
    print("**************************************")
    while True:
        choice = int(input('''
    Enter 1 to view your areas live data
    Enter 0 to quit
    '''))
        if choice == 1:

            api_key = 'b33b9693004ec7f5aa68c57be61c75ee'

            city = input("Enter your city (ex: Kigali): ")
            country_code = input("Enter country code (ex: RW): ")

            url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}&units=metric'
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                if 'main' in data:
                    print("Weather Data For Your Area")
                    print("***********************************")
                    temperature = data['main']['temp']
                    humidity = data['main']['humidity']
                    wind_speed = data['wind']['speed']
                    weather = data['weather'][0]['main']
                    description = data['weather'][0]['description']

                    print(
                        f"The weather in {city} is {weather} described by {description}")
                    print(f'The temperature in {city} is {temperature}°C.')
                    print(f'The humidity in {city} is {humidity}%.')
                    print(f'The wind speed in {city} is {wind_speed} m/s.')
                else:
                    print('Error: No "main" key in the API response.')
            else:
                print(
                    f'Error: API request failed with status code {response.status_code}.')
                print(response.text)
        else:
            break
