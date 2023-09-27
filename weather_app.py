import tkinter as tk
import requests
import json
from PIL import ImageTk, Image
import io  # Import the io module

def get_weather_data(city_id, appid):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "id": city_id,
        "appid": appid,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    weather_data = json.loads(response.content)
    return weather_data



class WeatherWidget(tk.Frame):
    def __init__(self, master, city_id, appid):
        super().__init__(master)

        # Get the weather data
        weather_data = get_weather_data(city_id, appid)

        # Extract the weather data from the JSON object
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        wind_direction = weather_data["wind"]["deg"]
        weather_condition = weather_data["weather"][0]["description"]

        # Load the weather icon image
        weather_icon_url = "https://openweathermap.org/img/wn/{}@2x.png".format(weather_data["weather"][0]["icon"])
        weather_icon_response = requests.get(weather_icon_url)
        weather_icon_image = Image.open(io.BytesIO(weather_icon_response.content))
        weather_icon_photoimage = ImageTk.PhotoImage(weather_icon_image)

        # Create the weather widget labels and images
        temperature_label = tk.Label(self, text=f"{temperature}°C", font=("Arial", 20))
        humidity_label = tk.Label(self, text=f"{humidity}% Humidity", font=("Arial", 14))
        wind_speed_label = tk.Label(self, text=f"{wind_speed} m/s Wind", font=("Arial", 14))
        wind_direction_label = tk.Label(self, text=f"{wind_direction}° Wind Direction", font=("Arial", 14))
        weather_condition_label = tk.Label(self, text=weather_condition, font=("Arial", 14))
        weather_icon_label = tk.Label(self, image=weather_icon_photoimage)
        weather_icon_label.image = weather_icon_photoimage  # Keep a reference to the image

        # Place the weather widget labels and images in the frame
        temperature_label.grid(row=0, column=0, sticky="nsew")
        humidity_label.grid(row=1, column=0, sticky="nsew")
        wind_speed_label.grid(row=2, column=0, sticky="nsew")
        wind_direction_label.grid(row=3, column=0, sticky="nsew")
        weather_condition_label.grid(row=4, column=0, sticky="nsew")
        weather_icon_label.grid(row=0, column=1, rowspan=5, sticky="nsew")

        # Set the frame background color to white
        self.config(bg="white")

    def update_weather_data(self):
        # Get the weather data
        weather_data = get_weather_data(city_id, appid)

        # Extract the weather data from the JSON object
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        wind_direction = weather_data["wind"]["deg"]
        weather_condition = weather_data["weather"][0]["description"]

        # Load the weather icon image
        weather_icon_url = "https://openweathermap.org/img/wn/{}@2x.png".format(weather_data["weather"][0]["icon"])
        weather_icon_response = requests.get(weather_icon_url)
        weather_icon_image = Image.open(io.BytesIO(weather_icon_response.content))
        weather_icon_photoimage = ImageTk.PhotoImage(weather_icon_image)

        # Create the weather widget labels and images
        temperature_label = tk.Label(self, text=f"{temperature}°C", font=("Arial", 20))
        humidity_label = tk.Label(self, text=f"{humidity}% Humidity", font=("Arial", 14))
        wind_speed_label = tk.Label(self, text=f"{wind_speed} m/s Wind", font=("Arial", 14))
        wind_direction_label = tk.Label(self, text=f"{wind_direction}° Wind Direction", font=("Arial", 14))
        weather_condition_label = tk.Label(self, text=weather_condition, font=("Arial", 14))
        weather_icon_label = tk.Label(self, image=weather_icon_photoimage)
        weather_icon_label.image = weather_icon_photoimage  # Keep a reference to the image

        # Place the weather widget labels and images in the frame
        temperature_label.grid(row=0, column=0, sticky="nsew")
        humidity_label.grid(row=1, column=0, sticky="nsew")
        wind_speed_label.grid(row=2, column=0, sticky="nsew")
        wind_direction_label.grid(row=3, column=0, sticky="nsew")
        weather_condition_label.grid(row=4, column=0, sticky="nsew")
        weather_icon_label.grid(row=0, column=1, rowspan=5, sticky="nsew")

        # Set the frame background color to white
        self.config(bg="white")

        root.after(60000, self.update_weather_data)



root = tk.Tk()

city_id = "184745"
appid = "2a317cbe1e9b338e96a973be7cfea14b"

# Create an instance of the weather widget
weather_widget = WeatherWidget(root, city_id, appid)

# Display the weather widget
weather_widget.pack()

# Start the mainloop
root.mainloop()
