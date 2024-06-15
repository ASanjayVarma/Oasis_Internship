import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import geocoder

def get_weather(city, units='metric'):
    api_key = "80b917f222c2526bf2b1606fb3b71b45"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units={units}"
    
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        wind = data["wind"]
        temperature = main["temp"]
        feels_like = main["feels_like"]
        humidity = main["humidity"]
        description = weather["description"]
        wind_speed = wind["speed"]

        unit_symbol = '°C' if units == 'metric' else '°F'
        wind_speed_unit = 'm/s' if units == 'metric' else 'mph'

        weather_info = (
            f"Temperature: {temperature}{unit_symbol}\n"
            f"Feels Like: {feels_like}{unit_symbol}\n"
            f"Humidity: {humidity}%\n"
            f"Description: {description.capitalize()}\n"
            f"Wind Speed: {wind_speed} {wind_speed_unit}"
        )
        weather_label.config(text=weather_info)

        if 'clear' in description.lower():
            icon_path = "Oasis weather\pics/sun.png"
        elif 'cloud' in description.lower():
            icon_path = "Oasis weather\pics/cloud.png"
        elif 'rain' in description.lower():
            icon_path = "Oasis weather\pics/cloud-rain.png"
        elif 'snow' in description.lower():
            icon_path = "Oasis weather\pics\cloud-snow.png"
        else:
            icon_path = "Oasis weather\pics\circle.png"

        icon_image = Image.open(icon_path)
        icon_image = icon_image.resize((60, 60), Image.LANCZOS)
        icon_image = ImageTk.PhotoImage(icon_image)
        icon_label.config(image=icon_image)
        icon_label.image = icon_image
    else:
        messagebox.showerror("Error", "City Not Found")

def get_location():
    g = geocoder.ip('me')
    return g.city if g.city else "Location Not Found"

def on_search():
    city = city_entry.get()
    if city:
        units = 'metric' if unit_var.get() == "Celsius" else 'imperial'
        get_weather(city, units)
    else:
        messagebox.showwarning("Input Error", "Please enter a city name")

def auto_detect_location():
    city = get_location()
    if city != "Location Not Found":
        city_entry.delete(0, tk.END)
        city_entry.insert(0, city)
        units = 'metric' if unit_var.get() == "Celsius" else 'imperial'
        get_weather(city, units)
    else:
        messagebox.showerror("Location Error", "Unable to detect location")

root = tk.Tk()
root.title("Weather Prediction App")
root.geometry("350x450")

city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=10)
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

unit_var = tk.StringVar(value="Celsius")
unit_frame = tk.Frame(root)
celsius_radio = tk.Radiobutton(unit_frame, text="Celsius", variable=unit_var, value="Celsius")
fahrenheit_radio = tk.Radiobutton(unit_frame, text="Fahrenheit", variable=unit_var, value="Fahrenheit")
celsius_radio.pack(side=tk.LEFT)
fahrenheit_radio.pack(side=tk.LEFT)
unit_frame.pack(pady=5)

auto_button = tk.Button(root, text="Auto Detect Location", command=auto_detect_location)
auto_button.pack(pady=5)

search_button = tk.Button(root, text="Search", command=on_search)
search_button.pack(pady=5)

weather_label = tk.Label(root, text="", font=("Helvetica", 12), justify=tk.LEFT)
weather_label.pack(pady=10)

icon_label = tk.Label(root, image=None)
icon_label.pack(pady=10)

root.mainloop()