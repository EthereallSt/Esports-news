from flask import Flask
from weather import weather_by_city

app = Flask(__name__)


@app.route('/')
def index():
    weather = weather_by_city('Moscow,Russia')
    if weather:
        weather_text = f'Погода в Москве на {weather["observation_time"]}, {weather["temp_C"]}, ощущается как {weather["FeelsLikeC"]}, скорость ветра = {weather["windspeedKmph"]}'
    else:
        weather_text = "Сервис временно недоступен"
    return f"""<html>
        <head>
            <title>Прогноз погоды</title>
        </head>
        <body>
            <h1> </h1>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)