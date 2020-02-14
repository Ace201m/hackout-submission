import requests
from bs4 import BeautifulSoup
import re

if __name__ == "__main__":
    
    url = "https://www.swiggy.com/dapi/restaurants/list/v5?lat=25.3176452&lng=82.9739144&page_type=DESKTOP_WEB_LISTING"

    params = {'lat':25.3176452,
                'lng':82.9739144,
                'page_type':'DESKTOP_WEB_LISTING'}
    res = requests.get(url, params=params)
    html = BeautifulSoup(res.text, 'html.parser')
    print(res.text)

