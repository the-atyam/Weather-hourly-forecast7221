import requests

def get_weather_forecast():
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=london,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_temperature_by_date(data, date):
    for item in data['list']:
        if date in item['dt_txt']:
            return item['main']['temp']
    return None

def get_wind_speed_by_date(data, date):
    for item in data['list']:
        if date in item['dt_txt']:
            return item['wind']['speed']
    return None

def get_pressure_by_date(data, date):
    for item in data['list']:
        if date in item['dt_txt']:
            return item['main']['pressure']
    return None

if __name__ == "__main__":
   
    weather_data = get_weather_forecast()

    while True:
        print("\nMenu:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            date = input("Enter the date in 'YYYY-MM-DD' format: ")
            temperature = get_temperature_by_date(weather_data, date)
            if temperature:
                print(f"Temperature on {date}: {temperature} K")
            else:
                print("Weather data not available for the given date.")
        elif choice == 2:
            date = input("Enter the date in 'YYYY-MM-DD' format: ")
            wind_speed = get_wind_speed_by_date(weather_data, date)
            if wind_speed:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Wind Speed data not available for the given date.")
        elif choice == 3:
            date = input("Enter the date in 'YYYY-MM-DD' format: ")
            pressure = get_pressure_by_date(weather_data, date)
            if pressure:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Pressure data not available for the given date.")
        elif choice == 0:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
