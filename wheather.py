import requests 
import subprocess
import random
import os 

# ANSI colour codes
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GREEN = "\033[32m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    CYAN = "\033[36m"
    MAGENTA = "\033[35m"

# Figlet ASCII function
def print_ascii_text():
    """Displays 'Weather' in a random FIGlet font, cowsay, or cowthink style."""
    COWSAY_CHARACTERS = [
        "cow", "dragon", "tux", "moose", "hellokitty"
    ]

    choice = random.choice(["figlet", "cowsay", "cowthink"])

    if choice == "figlet":
        font_list = os.popen("figlist").read().split()
        random_font = random.choice(font_list) if font_list else "standard"
        subprocess.run(["figlet", "-f", random_font, "Weather"])

    else:
        character = random.choice(COWSAY_CHARACTERS)
        subprocess.run([choice, "-f", character, "Weather"])

# OpenWeatherMap API details
API_KEY = "7efde8c2ac33412cd5f32d959bf21247"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    # Building the request URL
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "imperial"  # Use Fahrenheit
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Error fetching weather data:", e)
        return None

def display_weather(data):
    if data is None:
        print("No data to display.")
        return
    
    # Check if the API returned an error
    if data.get("cod") != 200:
        print("Error:", data.get("message", "Unable to fetch weather data"))
        return
    
    city = data.get("name")
    country = data.get("sys", {}).get("country")
    weather_desc = data.get("weather", [{}])[0].get("description", "No description")
    temp = data.get("main", {}).get("temp")
    humidity = data.get("main", {}).get("humidity")
    wind_speed = data.get("wind", {}).get("speed")

    print(f"\n{Colors.CYAN}Weather Stats for {city}, {country}:")
    print(f"{Colors.YELLOW}Description: {weather_desc.capitalize()}")
    print(f"{Colors.GREEN}Temperature : {temp} °F")
    print(f"{Colors.MAGENTA}Humidity: {humidity}%")
    print(f"{Colors.RED}Wind Speed: {wind_speed} mph")

if __name__ == "__main__":
    print_ascii_text()
    city = input("\nEnter city name: ").strip()
    weather_data = get_weather(city)
    display_weather(weather_data)
