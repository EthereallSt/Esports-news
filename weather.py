import requests

def weather_by_city(city_name):
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        "key": "0811b97620ea4a8982c110542222401",
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "showlocaltime": "yes",
        "lang": "ru"
    }
    try:
        result = requests.get(weather_url, params=params)
        weather = result.json()
        if 'data' in weather:   #Проверка есть ли дата в ответе
            if 'current_condition' in weather['data']:
                try:
                    return weather["data"]['current_condition'][0]   #правильный ход программы
                except(IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):
        print ("Сетевая ошибка")
        return False
    return False

if __name__ == "__main__":
    print(weather_by_city("Moscow,Russia"))

