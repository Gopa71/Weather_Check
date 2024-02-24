from django.shortcuts import render
from django.db.models import Q
import requests
# Create your views here.
def home(req):
    query = None
    weather_data = None
    if 'q' in req.GET:
        query = req.GET.get('q')
        api_key = '360e4bc3865e745ec844bd7ec054ca11'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={query}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
    return render(req,'index.html',{'query': query, 'weather_data': weather_data})


