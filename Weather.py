import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

def display_weather(weather_data):
    if weather_data:
        print(f"City: {weather_data['city']}")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Weather: {weather_data['description']}")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")
    else:
        print("Weather data not found. Please check the city name and try again.")

def main():
    api_key = "3746ad9b2aeb953b117a94ca8d578e56"
    while True:
        city = input("Enter the city name (or type 'exit' to quit): ")
        if city.lower() == 'exit':
            break
        weather_data = get_weather(api_key, city)
        display_weather(weather_data)
        input("Press Enter to check another city or type 'exit' to quit.")

if __name__ == "__main__":
    main()
