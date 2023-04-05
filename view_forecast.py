import requests


def viewForecast():
    print("Welcome To Weather Forecast Section")
    print("**************************************")
    while True:
        choice = int(input('''
            Enter 1 to view forecast for your area
            Enter 0 to quit
            '''))
        if choice == 1:

            api_key = 'b33b9693004ec7f5aa68c57be61c75ee'

            city_name = input("Enter your city (ex: Kigali): ")
            country_code = input("Enter country code (ex: RW): ")

            url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name},{country_code}&appid={api_key}"
            response = requests.get(url)
            data = response.json()
            forecast = data["list"]

            headers = ("Date/Time", "Temperature (K)", "Weather Description")
            print("Weather Forecasts For The Next Five days At Various Times")
            print("***************************************************************")
            print("{:<25} {:<18} {:<25}".format(*headers))
            for item in forecast:
                date_time = item["dt_txt"]
                temperature = item["main"]["temp"]
                description = item["weather"][0]["description"]

                print("{:<25} {:<18} {:<25}".format(
                    date_time, temperature, description))
        else:
            break
