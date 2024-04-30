# weather_app/views.py
from django.shortcuts import render
import requests

def get_weather(request):
    api_key = 'BG4CN8rN1NokZrlNE3AEU2TbVVdV8fcK'  # Replace with your Open-Meteo API key
    latitude = 46.8772  # Fargo's latitude
    longitude = -96.7898  # Fargo's longitude

    url = f"https://api.open-meteo.com/weather?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    headers = {'Authorization': f'Bearer {api_key}'}

    response = requests.get(url, headers=headers)
    data = response.json()

    temperature = data['hourly']['temperature_2m'][0]['value']
    time = data['hourly']['time'][0]

    context = {
        'temperature': temperature,
        'time': time
    }

    return render(request, 'home.html', context)
