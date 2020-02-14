from bs4 import BeautifulSoup
import requests, json

link = "https://www.swiggy.com/restaurants/al-baik-world-ravindrapuri-lanka-varanasi-78246"
link2 = "https://www.swiggy.com/restaurants/capsicum-lanka-varanasi-88160"

res = requests.get(link2)

soup = BeautifulSoup(res.text, 'html.parser')
# # print(soup.prettify())
# f = open("res.html",'w+')
# f.write(soup.prettify())
# f.close()

res = soup.find_all('script')
# str(res[3])[35:-9]
dic = json.loads(str(res[3])[35:-9])
print(dic)
# print(str(res[4])[104:-10])


def getRestaurant(link):
    





class Restaurent:

    def __init__(self, link):

        res = requests.get(link)
        res = BeautifulSoup(res.text, 'html.parser')
        res = soup.find_all('script')
        tempDict = json.loads(str(res[3])[35:-9])


        self.name = tempDict['name']
        self.city = tempDict['address']['addressRegion']
        self.image = tempDict['imagepprint']
        self.cuisine = tempDict['serves']
        self.rating = tempDict['aggregateRating']['ratingValue']
        self.rate_count = tempDict['aggregateRating']['ratingCount']
        self.locality = locality
        self.price_range = price_range

    def __str__(self):
        return self.name + ", "+ self.locality + ", " + self.city
        


        