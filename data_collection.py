from src.model.Restaurent import Restaurent
from src.model.Food import Food
import pickle

import requests
from pprint import pprint


myDict = {}

if __name__ == "__main__":

    api_link = r"https://test-es.edamam.com/search?q={}&app_id=3e3dc607&app_key=14976a9356fa2d90fec6beb3ce89855c"

    dishes = []
    restaurents = []
    with open('rest_link.txt') as f:
        for link in f.readlines():
            print(link)
            rest = Restaurent(link)
            restaurents.append(rest)
            for food in rest.getFoodList():
                dishes.append(food)

    with open('food_dataset.pkl', 'wb') as f:
        pickle.dump(dishes, f)    

    with open('rest_dataset.pkl', 'wb') as f:
        pickle.dump(restaurents, f)
