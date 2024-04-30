# weather_App/views.py
import requests
from django.shortcuts import render
from django.conf import settings

def weather(request):
    api_key = settings.OPENWEATHERMAP_API_KEY
    api_endpoint = settings.OPENWEATHERMAP_API_ENDPOINT
    city = 'Fargo,US'  # Example city
    units = 'metric'  # Example units

    url = f"{api_endpoint}?q={city}&units={units}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    context = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description']
    }
    return render(request, 'home.html', context)
