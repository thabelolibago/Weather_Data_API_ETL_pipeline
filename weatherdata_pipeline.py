import requests
import json
import pandas as pd

# OpenWeather API key.
api_key = "2d8fef17a92a4ef3839c7fcea8fb98db"

# Get the city from the user.
city_name = input("Enter a city: ")

# Get the weather data for today.
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
response = requests.get(url)

# Check the response status code.
if response.status_code != 200:
    raise Exception(f"Error fetching weather data: {response.status_code}")

# Get the weather data as a JSON object.
weather_data = json.loads(response.content)

# Get the temperature.
temperature = weather_data["main"]["temp"]

# Get the humidity.
humidity = weather_data["main"]["humidity"]

# Get the pressure.
pressure = weather_data["main"]["pressure"]

# Print the weather data.
print(f"Temperature: {temperature}°C")
print(f"Humidity: {humidity}%")
print(f"Pressure: {pressure} hPa")

# Save the output as a CSV file.
df = pd.DataFrame({"Temperature": [temperature], "Humidity": [humidity], "Pressure": [pressure]})
df.to_csv("weather_data.csv")

# Add a comment to the top of the code.
"""
This code gets the weather data for a city and prints the temperature, humidity, and pressure.
"""