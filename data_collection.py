from src.model.Restaurent import Restaurent
from src.model.Food import Food

import requests

if __name__ == "__main__":

    api_link = r"https://test-es.edamam.com/search?q={}&app_id=3e3dc607&app_key=14976a9356fa2d90fec6beb3ce89855c"

    dishes = set()
    with open('rest_link.txt') as f:
        for link in f.readlines():
            print(link)
            rest = Restaurent(link)
            for food in rest.getFoodList():
                dishes.add(food.getCategory())

    print(len(dishes))
    print(dishes)
                