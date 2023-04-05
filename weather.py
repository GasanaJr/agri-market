import view_weather
import crop_suggestion
import view_forecast


def weather():

    while True:
        print("Welcome to Weather & Climate Section")
        print("*******************************************")
        choice = int(input('''
            Enter 1 to view Live weather data
            Enter 2 to view Weather Forecast
            Enter 3 for crop suggestion
            Enter 0 to quit()
        '''))

        if choice == 1:
            view_weather.viewWeather()
        elif choice == 3:
            crop_suggestion.cropSuggestion()
        elif choice == 2:
            view_forecast.viewForecast()
        else:
            break
