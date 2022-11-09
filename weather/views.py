from django.shortcuts import render
import requests, sys
from django.http import HttpResponse
from django.conf import settings

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
CITY = 'Seattle' #validate and could be more arguments
# Create your views here.
def main(request):
    url = f'{BASE_URL}q={CITY}&APPID={settings.API_KEY}'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print("Http Error:", err)
        sys.exit('Try agin with Valid city.')

    response = response.json()

    description = response['weather'][0]['description']
    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
     
    result = f'\n{CITY}: {temp_celsius}°C / {temp_fahrenheit}°F {description}\n'
    print(result)
    
    return HttpResponse(result)

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
