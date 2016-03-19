import urllib2
import json
import app

def geturl(city='nyc'):
    url = 'http://api.openweathermap.org/data/2.5/find?q=' + city + '&APPID=00f50410f3be76791e8080677ad6df97&units=imperial'
    u = urllib2.urlopen( url )
    global result
    result = json.loads(u.read())

def get_weather_temp(city='nyc'):
    geturl(city)
    print result    
    return result['list'][0]['main']['temp']

def get_weather_humidity(city='nyc'):
    geturl(city)
    print result
    return result['list'][0]['main']['humidity']

def get_weather_windspeed(city='nyc'):
    geturl(city)
    print result
    return result['list'][0]['wind']['speed']

def get_weather_tempminmax(city='nyc'):
    geturl(city)
    print result
    mintemp = result['list'][0]['main']['temp_min']
    maxtemp = result['list'][0]['main']['temp_max']
    if mintemp == maxtemp:
        return 'not currently available; neither is the maximum temperature. Blame OpenWeatherMap, not me'
    else:
        return str(mintemp) + ' degrees Farenheit and the maximum temperature is ' + str(maxtemp) + ' degrees Farenheit'

def get_country(city='nyc'):
    geturl(city)
    print result
    return result['list'][0]['sys']['country']

def get_real_city(city='nyc'):
    geturl(city)
    print result
    return result['list'][0]['name']
