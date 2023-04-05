import file
import start
import weather

ussd = input("Enter USSD ")

if (ussd == '*171#'):
    file.main_file()
elif (ussd == '*172#'):
    start.start()
elif (ussd == '*173#'):
    weather.weather()
