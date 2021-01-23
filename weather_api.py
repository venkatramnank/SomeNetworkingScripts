import requests
import re
cityname=input("Enter the city name :")
r= requests.get("http://api.openweathermap.org/data/2.5/weather?appid=c9cc431a11c9bf05cc82aee6b6cc08dd&q="+cityname+"&units=metric")
x=r.json()
if x['cod']!=0:
        y=x['main']
        hum=y['humidity']
        y=x.get('weather')
        str=(y[0]).get('description')
        if(re.search('clouds',str)):
            print('Take umbrella with you')
        elif(hum>90):
            print('Take umbrella with you')
            