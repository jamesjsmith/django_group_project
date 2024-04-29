
# Create your views here.

import requests
from django.shortcuts import render

def weather(request):
    #Make a GET request to the API
    url = "https://api.weather.gov/gridpoints/FGF/65,51/forecast"
    response = requests.get(url)
    
    #Check if request was successful
    if response.status_code == 200:
        data = response.json()
        
        forecast = data["properties"]["periods"]
       
        return render(request, 'weather/weather.html', {'forecast': forecast})
    else:
        error_message = "Failed to fetch weather data."
        return render(request, 'weather/error.html', {'error_message': error_message})
