from bs4 import BeautifulSoup
import requests, json
from .Food import Food

link = "https://www.swiggy.com/restaurants/al-baik-world-ravindrapuri-lanka-varanasi-78246"
link2 = "https://www.swiggy.com/restaurants/capsicum-lanka-varanasi-88160"

# str(res[3])[35:-9]
# print(str(res[4])[104:-10])


class Restaurent:

    def __init__(self, link):

        res = requests.get(link)
        res = BeautifulSoup(res.text, 'html.parser')
        res = res.find_all('script')
        tempDict = json.loads(str(res[3])[35:-9])


        self.name = tempDict['name']
        self.city = tempDict['address']['addressRegion']
        self.image = tempDict['image']
        self.cuisine = tempDict['servesCuisine']
        try:
            self.rating = tempDict['aggregateRating']['ratingValue']
            self.rate_count = tempDict['aggregateRating']['ratingCount']
        except:
            pass
        self.locality = tempDict['address']['addressLocality']  
        self.price_range = tempDict['priceRange']
        self.food_items = []

        data = json.loads(str(res[4])[104:-(2015)])
        temp_food_items = data['menu']['items']
        for i in temp_food_items:
            newFoodItem = Food(temp_food_items[i], self.name, self.image)
            self.food_items.append(newFoodItem)

    def getImage(self):
        return self.image

    def getFoodList(self):
        return self.food_items

    def __str__(self):
        return self.name + ", "+ self.locality + ", " + self.city + ', first food - '+ str(self.food_items[0]) +", size ="+ str(len(self.food_items))
        


        