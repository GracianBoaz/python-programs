class Weather:
    def __init__(self, location, temperature=0.0, humidity=0.0):
        """
        Initialize the Weather class with location, temperature, and humidity.
        The temperature and humidity default to 0.0 if not provided.
        """
        self.location = location
        self.temperature = temperature
        self.humidity = humidity

    def update_weather(self, temp, hum):
        """
        Updates the temperature and humidity.
        """
        self.temperature = temp
        self.humidity = hum
        print(f"Weather updated: Temperature = {self.temperature}°C, Humidity = {self.humidity}%")

    def display_weather(self):
        """
        Displays the weather details in a formatted way.
        """
        print(f"Weather Report for {self.location}:")
        print(f"Temperature: {self.temperature}°C")
        print(f"Humidity: {self.humidity}%")

# Example Usage
# Create a Weather object for a specific location
weather_report = Weather("New York")

# Display initial weather details
weather_report.display_weather()

# Update weather details (temperature and humidity)
weather_report.update_weather(25.3, 60)

# Display updated weather details
weather_report.display_weather()
