import requests

class WeatherAPIController:
    def __init__(self, api_key:str, unit:str) -> None:

        """
        Initializes the WeatherAPIController class with the specified API key and unit of measurement.
        
        Args:
            api_key (str): The API key for accessing the OpenWeatherMap API.
            unit (str): The unit of measurement for temperature (e.g., 'metric' for Celsius, 'imperial' for Fahrenheit).
        """

        self.api_key = api_key
        self.unit = unit

    def get_location(self) -> dict:

        """
        Retrieves the current location data using the IPInfo service.
        
        Returns:
            dict: A dictionary containing the city, latitude, and longitude of the current location.
        """

        try:
            print('Trying to get the location data')
            response = requests.get("https://ipinfo.io")
            data = response.json()
            
            location_data ={
                 'City': data['city'],
                 'Latitude': data['loc'].split(',')[0],
                 'Longtitude': data['loc'].split(',')[1]
            }

            print('Location found succesfully!')
            return location_data
        
        except Exception as e:
            print(f"[ get_location ] Error: {e}")

    def get_weather(self, city) -> dict:

        """
        Retrieves the weather data for the specified city using the OpenWeatherMap API.
        
        Args:
            city (str): The name of the city for which to retrieve weather data.
        
        Returns:
            dict: A dictionary containing weather information such as temperature, pressure, humidity, weather description, and wind speed.
        """
        
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': self.api_key,
            'lang': 'tr',
            'units': self.unit
        }
        try:
            print('Trying to get weather data')
            response = requests.get(base_url, params=params)
            data = response.json()
            
            if response.status_code == 200:
                main = data['main']
                weather = data['weather'][0]
                wind = data['wind']
                weather_info = {
                    'City': city,
                    'Temperature': main['temp'],
                    'Pressure': main['pressure'],
                    'Humidity': main['humidity'],
                    'Weather': weather['description'],
                    'Wind Speed': wind['speed']
                }
                print(weather_info)
                print('Weather data gathered succesfuly')
                return weather_info
        except:
            return f"[ get_weather ] Error: {data['message']}"
        