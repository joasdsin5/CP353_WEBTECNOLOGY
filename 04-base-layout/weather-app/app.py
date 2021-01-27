from flask import Flask
from flask import render_template
from flask import request
from urllib.parse import quote
from urllib.request import urlopen
import json

app = Flask(__name__)

OPEN_WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?q={0}&units=metric&APPID={1}"

OPEN_WEATHER_KEY = '456c1a3c436150042b033dd0e6261e4a'

@app.route("/")
def home():
    city = request.args.get('city')
    if not city:
        city = 'bangkok'
    weather = get_weather(city, OPEN_WEATHER_KEY)

    return render_template("home.html", weather=weather)


def get_weather(city,API_KEY):
    query = quote(city)     #ทำให้เวลามี space มาก็ไปเติม string ให้ทำให้ url รันได้

    url = OPEN_WEATHER_URL.format(city, API_KEY)    #แทนที่ {0}, {1}

    data = urlopen(url).read()  #ยิง req แล้วจะตอบกลับมาเป็น json


    parsed = json.loads(data)


    weather = None
    if parsed.get('weather'):   #ใช้ในกรณี idkey ผิด

        description = parsed['weather'][0]['description']
        temperature = parsed['main']['temp']
        city = parsed['name']
        country = parsed['sys']['country']

        weather = {'description': description,
                   'temperature': temperature,
                   'city': city,
                   'country': country
                   }
    return weather
