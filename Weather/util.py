import urllib2
import json

def get_weather_temp(city='nyc'):
    url = 'http://api.openweathermap.org/data/2.5/find?q=' + city + '&APPID=00f50410f3be76791e8080677ad6df97&units=imperial'
    u = urllib2.urlopen( url )
    result = json.loads(u.read())

    print result    
    return result['list'][0]['main']['temp']

def get_weather_humidity(city='nyc'):
    url = 'http://api.openweathermap.org/data/2.5/find?q=' + city + '&APPID=00f50410f3be76791e8080677ad6df97&units=imperial'
    u = urllib2.urlopen( url )
    result = json.loads(u.read())

    print result
    return result['list'][0]['main']['humidity']

def get_weather_windspeed(city='nyc'):
    url = 'http://api.openweathermap.org/data/2.5/find?q=' + city + '&APPID=00f50410f3be76791e8080677ad6df97&units=imperial'
    u = urllib2.urlopen( url )
    result = json.loads(u.read())

    print result
    return result['list'][0]['wind']['speed']

def get_weather_tempminmax(city='nyc'):
    url = 'http://api.openweathermap.org/data/2.5/find?q=' + city + '&APPID=00f50410f3be76791e8080677ad6df97&units=imperial'
    u = urllib2.urlopen( url )
    result = json.loads(u.read())

    print result
    mintemp = result['list'][0]['main']['temp_min']
    maxtemp = result['list'][0]['main']['temp_max']
    if mintemp == maxtemp:
        return 'not currently available; neither is the maximum temperature'
    else:
        return str(mintemp) + ' degrees Farenheit and the maximum temperature is ' + str(maxtemp) + ' degrees Farenheit'
