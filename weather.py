import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if data["cod"] == "404":
        print("Location not found. Please try again.")
        return

    weather = data["weather"][0]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_description = weather["description"]

    print("\nCurrent Weather Conditions:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {weather_description.capitalize()}")

def main():
    api_key = "27e6c2ebbd96a4c9842fd67d7b52a23d"  # Replace "YOUR_API_KEY" with your actual API key
    location = input("Enter city name or ZIP code: ")

    weather_data = get_weather(api_key, location)

    display_weather(weather_data)

if __name__ == "__main__":
    main()
