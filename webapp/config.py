import os

basedir = (os.path.abspath(os.path.dirname(__file__)))   

WEATHER_DEFAULT_CITY = "Moscow,Russia"
WEATHER_API_KEY = "0811b97620ea4a8982c110542222401"
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')