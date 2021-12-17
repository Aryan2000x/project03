import requests
from django.shortcuts import render
from .models import City


# Define the home view

def index(request):
  url= "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=615565f33a31c50af502c7ff0810f560"

  city = 'Toronto'

  cities = City.objects.all()

  weather_data = []
   
  for city in cities:

      r = requests.get(url.format(city)).json()

      city_weather = {
          'city': city.name ,
          'temperature': r['main']['temp'],
          'description' : r ['weather'][0]['description'],
          'icon': r['weather'][0]['icon'],
      }

      weather_data.append(city_weather)

  print(weather_data)

  context = {'weather_data': weather_data}

  return render(request, 'weather/weather.html', context)
