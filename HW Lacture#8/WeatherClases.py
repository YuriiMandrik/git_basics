from urllib.request import urlopen
import json
from Exeptions import CityNameError, CoordError
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
TOKEN = '18c6e0f43541c0148fa43fbd483f79b4'


class City():
    def __init__(self, name, latitude=None, longitude=None):
        self._name = name
        self._latitude = latitude
        self._longitude = longitude
        if self._latitude is None and self._longitude is None:
            self.set_coords()

    def get_coords(self):
        if self._name.isalpha():
            url = f'http://api.openweathermap.org/geo/1.0/direct?q={self._name}&appid={TOKEN}'
            response = urlopen(url)
            data = response.read()
            data = data.decode('utf-8')
            res = json.loads(data)
            lat = res[0]['lat']
            lon = res[0]['lon']
        else:
            raise CityNameError


        return lat, lon

    def set_coords(self):
        self._latitude, self._longitude = self.get_coords()

    def __str__(self):
        return f'City {self._name} has latitude:{self._latitude} ' \
               f'and longitude{self._longitude}'


class Weather():

    def __init__(self, city, coords=None):
        self.city = city
        self.coords = coords

    def current_weather(self):
        if self.coords:
            try:
                float(self.coords[0])
                float(self.coords[1])
            except ValueError:
                raise CoordError()


        else:
            self.coords = City(self.city).get_coords()

        url = f'https://api.openweathermap.org/data/2.5/weather?lat={self.coords[0]}&lon={self.coords[1]}&units=metric&appid={TOKEN}'
        response = urlopen(url).read().decode('utf-8')
        res = json.loads(response)
        # print(res)
        return (f"Температура: {res['main']['temp']} "
                f"відчувається як: {res['main']['feels_like']} "
                f"швидкість вітру: {res['wind']['speed']}")

    def __str__(self):
        return self.current_weather()




