# # # # # #
# * Weather App * #
# * User should enter a city name with it's country code
# * GeoCodingAPI : https://api.openweathermap.org/geo/1.0/direct?q={city},{countryCode}&limit=0&appid={APIKEY}
# * WeatherAPI : https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&units=metric&appid={APIKEY}
# # # # # #

from datetime import datetime
from datetime import timezone as tz
from os import environ
from re import sub

from dotenv import load_dotenv
from requests import get as GET


# # Loading environment variables from .env file into os.environ
load_dotenv()
APIKEY = environ.get('APIKEY')

# # Base URLs
base_geo_url = f'https://api.openweathermap.org/geo/1.0/direct?appid={APIKEY}&limit=0&'
base_weather_url = f'https://api.openweathermap.org/data/2.5/forecast?appid={APIKEY}&units=metric&'


max_chars = 75


def print_error(error_message: str):
    '''Prints the error message in a formatted way'''

    print('\n' + f'  {error_message}  '.center(max_chars, '✕') + '\n')


def print_line(char='⁘'):
    '''Prints a line in a formatted way'''

    print('\n' + ''.center(max_chars, char))


def welcome_message():
    '''Prints the Welcome Message for mausam.py'''

    print_line()
    print('\n'+'Welcome to Mausam'.center(max_chars, ' '))
    print('Your Personal Weather Assistant'.center(max_chars, ' '))
    print('Powered by OpenWeatherMap'.center(max_chars, ' '))
    print_line()


def clean_input(user_input):
    '''Cleans the user input by removing extra spaces and commas and returns in a fomatted way, i.e. city,country_code'''

    no_space_input = sub(r'\s+|,+', ',', user_input.lower())
    clean_input = sub(r',+', ',', no_space_input).strip(',')

    return clean_input


def get_coordinates(city):
    '''Returns the latitude and longitude of the city'''

    geo_response = GET(base_geo_url + f'q={city}')
    if (geo_response.status_code != 200):  # checking if the API call was successful
        raise Exception('Something went wrong | Fetching Coordinates')

    geo_data = geo_response.json()
    if (len(geo_data) == 0):  # checking if the city is found or not
        raise Exception('Not Found | City')

    return (geo_data[0]['lat'], geo_data[0]['lon'])


def get_weather_info(lat, lon):
    '''Returns the weather information of the city'''

    weather_response = GET(base_weather_url + f'lat={lat}&lon={lon}')
    if (weather_response.status_code != 200):  # checking if the API call was successful
        raise Exception('Something went wrong | Fetching Weather Info')

    weather_data = weather_response.json()
    if (len(weather_data['list']) == 0):  # checking if the weather is found or not
        raise Exception('Not Found | Weather Data')

    return {
        'city': weather_data['city']['name'],
        'country': weather_data['city']['country'],
        'timezone': weather_data['city']['timezone'],
        'weather_list': weather_data['list'],
    }


def extract_weather_by_days(weather_list, timezone):
    '''Returns the weather information by days'''

    weather_day = datetime.fromtimestamp(weather_list[0]['dt'] + timezone, tz.utc)
    one_day_weather = []
    weather_by_days = []

    for weather in weather_list:
        date = datetime.fromtimestamp(weather['dt'] + timezone,  tz.utc).day
        if date == weather_day.day:
            one_day_weather.append(weather)
        else:
            weather_day = datetime.fromtimestamp(weather['dt'] + timezone, tz.utc)
            weather_by_days.append(one_day_weather)
            one_day_weather = [weather]

    return weather_by_days


def print_weather(city, country, weather_list, timezone):
    '''Prints the weather information'''

    weather_day = datetime.fromtimestamp(weather_list[0]['dt'] + timezone, tz.utc)
    avg_temp = 0
    avg_min = 0
    avg_max = 0
    avg_temp_feels = 0

    print_line('—')
    print(
        '\n' + f"{city}, {country} | Weather Forcast",
        '\n' + f"{weather_day.strftime('%d %b, %Y')}" + '\n',
    )

    for weather in weather_list:
        avg_temp += weather['main']['temp']
        avg_min += weather['main']['temp_min']
        avg_max += weather['main']['temp_max']
        avg_temp_feels += weather['main']['feels_like']

        date = datetime.fromtimestamp(weather["dt"] + timezone, tz.utc)
        print(
            date.strftime('%I:%M%p\t'),
            f"{weather['main']['temp']:.1f}°C\t",
            weather['weather'][0]['description'].title()
        )

    avg_temp /= len(weather_list)
    avg_min /= len(weather_list)
    avg_max /= len(weather_list)
    avg_temp_feels /= len(weather_list)

    print(
        '\n'+'Averages '.ljust(int(max_chars // 2), '⁘'),
        f'\nTemperature : {avg_temp:.1f}°C',
        f'\nMinimum : {avg_min:.1f}°C',
        f'\nMaximum : {avg_max:.1f}°C',
        f'\nTemperature Feel : {avg_temp_feels:.1f}°C',
    )
    print_line('—')


welcome_message()  # printing the welcome message

while True:
    print('\nEnter the city name & country code (e.g. Lucknow,IN)')
    print('OR \'q\' to quit.')
    user_input = input('※ ')

    user_input = clean_input(user_input)  # cleaning the user input

    if user_input in ['q', 'quit', 'exit']:  # checking if the user wants to quit
        break

    # getting the coordinates
    try:
        lat, lon = get_coordinates(user_input)
    except Exception as e:
        print_error(str(e))
        continue

    # getting the weather infomation
    try:
        weather_info = get_weather_info(lat, lon)
    except Exception as e:
        print_error(str(e))
        continue

    # extracting the weather information by days
    weather_by_days = extract_weather_by_days(weather_info['weather_list'], weather_info['timezone'])

    # printing the weather information for today
    print_weather(
        weather_info['city'], weather_info['country'], weather_by_days[0], weather_info['timezone']
    )
