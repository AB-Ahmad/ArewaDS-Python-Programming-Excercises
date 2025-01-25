from dotenv import load_dotenv
import os
import requests
from pprint import pprint

load_dotenv()

def Get_Weather(city = "Abuja"):

    requests_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_key")}&q={city}&units=metric'
 
    #print(requests_url)
    weather_info = requests.get(requests_url).json()
    #pprint(weather_info)
    return weather_info

if __name__ == "__main__":
    print("\n ***Get Weather data in real time***\n")
    city = input("\nEnter the city\n")
    weather_info = Get_Weather(city)
    print("\n")
    pprint(weather_info["main"])






Get_Weather()
Get_Weather("kano")