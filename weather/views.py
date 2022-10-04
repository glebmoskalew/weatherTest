import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


appid = '3e7d84d01173bcca007e2b4a6a566723'
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid


def request_weather(city_name):
    # TODO: use urlquote ищи экранирование параметров в url
    return requests.get(url.format(city_name)).json()


def index(request):

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        # TODO: не делать запрос сразу (только при вводе пользователем города)
        #   выводить записи из БД у которых date > now - 2h
        # if request.method == 'POST':
            # TODO: только для города который ввел пользователь
        res = request_weather(city.name)
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }

    all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)

# Create your views here.
