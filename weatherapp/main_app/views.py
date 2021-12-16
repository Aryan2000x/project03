import requests
from django.shortcuts import render


# Define the home view

<<<<<<< HEAD
def about(request):
    return render(request, 'about.html')
=======
def index(request):
  url= "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=615565f33a31c50af502c7ff0810f560"

  city = 'Toronto'

  r = requests.get(url.format(city)).json()

  city_weather = {
    'city': city ,
    'temperature': r['main']['temp'],
    'description' : r ['weather'][0]['description'],
    'icon': r['weather'][0]['icon'],
  }
  
  context = {'city_weather': city_weather}

  return render(request, 'weather/weather.html', context)
    

>>>>>>> master
