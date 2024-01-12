import requests
import tkinter as tk
from tkinter import messagebox

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.location_label = tk.Label(root, text="Enter City:", font=('Arial', 16))
        self.location_label.pack(pady=10)

        self.location_entry = tk.Entry(root, font=('Arial', 14))
        self.location_entry.pack(pady=10)

        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather, font=('Arial', 14), bg='#4CAF50', fg='white')
        self.get_weather_button.pack(pady=10)

        self.weather_label = tk.Label(root, text="", font=('Arial', 14), wraplength=300)
        self.weather_label.pack(pady=10)

    def get_weather(self):
        city = self.location_entry.get()

        if not city:
            messagebox.showwarning("Warning", "Please enter a city.")
            return

        api_key = '4906fb074b72a5b7676e82af647c321e'
        base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        try:
            response = requests.get(base_url)
            data = response.json()

            if response.status_code == 200:
                weather_description = data['weather'][0]['description']
                temperature = data['main']['temp']
                wind_speed = data['wind']['speed']

                result = f"Weather: {weather_description}\nTemperature: {temperature}°C\nWind Speed: {wind_speed} m/s"
                self.weather_label.config(text=result)
            else:
                messagebox.showerror("Error", f"Failed to get weather data. {data['message']}")

        except requests.ConnectionError:
            messagebox.showerror("Error", "Failed to connect to the weather service.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.geometry("400x300")
    root.configure(bg='#F5F5F5')  # Light gray background
    root.mainloop()
