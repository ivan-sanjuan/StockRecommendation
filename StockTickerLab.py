from PIL import Image
import requests
import json


def country_input():
    name = input('Enter Country here: ')
    url = f'https://restcountries.com/v3.1/name/{name}?fullText=true'
    response: list[dict] = requests.get(url)
    data = response.json()
    country_name: str = data[0]['name']['common']
    country_cap: str = data[0]['capital'][0]
    country_curr: str = list(data[0]['currencies'].values())[0]['name']
    country_alt: str = data[0]['altSpellings'][1]
    country_lock: bool = data[0]['landlocked']
    country_area: int = data[0]['area']
    country_maps: str = data[0]['maps']['googleMaps']

    return country_name, country_cap, country_curr, country_alt, country_lock, country_area, country_maps


class Country():
    def __init__(self, name, cap, curr, alt, lock, area, maps):
        self.name: str = name
        self.cap: str = cap
        self.curr: str = curr
        self.alt: str = alt
        self.lock: bool = lock
        self.area: int = area
        self.maps: str = maps
        
    def __str__(self):
                return f'''This is {self.name}.
                The capital of {self.name} is {self.cap}.
                The currency that they have is the {self.curr}.
                People also refer to {self.name} as {self.alt}
                Are they landlocked you ask? {self.lock},
                and they have an area of around {self.area:,.2f}
                take a look of them in {self.maps}'''
        
country_1_data = country_input()
country_1 = Country(*country_1_data)
country_2_data = country_input()
country_2 = Country(*country_2_data)

print(country_1)
print(country_2)
