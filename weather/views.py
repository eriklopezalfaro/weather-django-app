from django.shortcuts import render, redirect
import requests, sys
from django.http import HttpResponse
from django.conf import settings
from .forms import CityForm
import pprint

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
# CITY = 'Seattle' #validate and could be more arguments
# Create your views here.
def main(request):
    # return HttpResponse(result)
    # add context holding local weather
    return redirect('city_name')

def get_data(city):
    url = f'{BASE_URL}q={city}&APPID={settings.API_KEY}'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print("Http Error:", err)
        sys.exit('Try agin with Valid city.')

    response = response.json()
    pprint.pprint(response, indent=2)


    description = response['weather'][0]['description']
    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
     
    # make and object and use .as_p in html, also make decimal smaller
    # result = f'City: {city} Temperature °C / °F: {temp_celsius}°C / {temp_fahrenheit}°F Description: {description}'
    result = {
        'name':city, 
        'temp_celcius':temp_celsius,
        'temp_fahrenheit':temp_fahrenheit,
        'description':description,
        'main':response['main'],
    }

    pprint.pprint(result['main'], indent=2)

    return result

def city_name(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data.get('city_name')
            city_format = get_data(city)

            print('valid..')
            # process the data in form.cleaned_data as required
            # print('=================',get_data(city), '------------------------------')
            return render(request, "weather/base.html", {'form':form, 'city':get_data(city)})

    else:
        form = CityForm()

    return render(request, "weather/base.html", {'form':form})
    

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return format(celsius, '.2f'), format(fahrenheit, '.2f')



if __name__ == '__main__':
    main()
