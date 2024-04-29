
import requests
from django.shortcuts import render

def home(request):
    api_key = "ccc10b2fd58aec6030233953a7c5fa63"
    city = "Fargo,ND"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    print(data)
    weather_data = {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"]
    }

    return render(request, "home.html", {"weather_data": weather_data})
