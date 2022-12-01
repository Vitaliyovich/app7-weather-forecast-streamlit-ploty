import requests

API_KEY = '172f86ddd0111719de647a5b2a7ad6a0'


def get_data(place, forecast_days=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]

    return filtered_data


if __name__ == '__main__':
    print(get_data(place='Lviv', forecast_days=1))
