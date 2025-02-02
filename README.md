# Weatherly

# 🌤️ **Weather App with Colorful Output and ASCII Art** 🌈

## Overview

This Python script fetches weather data from the OpenWeatherMap API and displays it in a beautiful format using dynamic ASCII art. The output includes colorful weather stats, including temperature, humidity, and wind speed, and is formatted with random ASCII styles such as `figlet` or `cowsay/cowthink`. This provides a fun and visually appealing way to check the weather.

## Features

- 🌍 **Fetches weather data** using the OpenWeatherMap API.
- ☁️ **Displays the weather stats** in a clean, readable format, including:
  - 🌡️ **Temperature** (in Fahrenheit)
  - 💧 **Humidity**
  - 🌬️ **Wind Speed**
- 🎨 **Dynamic ASCII Art**: Displays the word "Weather" in a random style using:
  - `figlet` with a random font from available fonts.
  - `cowsay/cowthink` with random characters (like cow, dragon, tux, moose, and hellokitty).
- 🌈 **Colorful Output**: Weather stats are shown in bright colors for clarity.

## Requirements

- Python 3.x
- Python modules: `requests`, `subprocess`, `os`, and `random`
- External utilities: `figlet`, `cowsay`, `cowthink`

### Optional:
- Install `figlet` and `cowsay` for full functionality:
  - **On Ubuntu/Debian**:
    ```bash
    sudo apt install figlet cowsay
    ```
  - **On macOS** (using Homebrew):
    ```bash
    brew install figlet cowsay
    ```
  - **On Arch Linux**:
    ```bash
    sudo pacman -S figlet cowsay
    ```

## Installation

1. **Clone or download the repository** to your local machine.

2. **Install Python dependencies** (if not already installed):

    ```bash
    pip install requests
    ```

3. **Ensure `figlet` and `cowsay` are installed** for full functionality (if they aren't already installed on your system).

## Usage

1. **Run the script**:

    ```bash
    python weather_app.py
    ```

2. **Enter the city name** when prompted to get the current weather for that city.

    Example:
    ```
    Enter city name: London
    ```

3. The weather information will be displayed in a colorful format, with ASCII art at the top.

### Sample Output:

```bash
  _       __     __         _
 / |      \ \   / /  _   _  | |
 | |     __\ \_/ /__| |_| | | |
 | |    / __   _/ __|     | | |
 |_|   /_/  \_/\__  \____/  |_|      
Weather Stats for London, GB:
Description: Light rain
Temperature : 55.9 °F
Humidity: 72%
Wind Speed: 4.56 mph

