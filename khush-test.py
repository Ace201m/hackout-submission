from bs4 import BeautifulSoup
import requests, json
from pprint import pprint

link = "https://www.swiggy.com/restaurants/al-baik-world-ravindrapuri-lanka-varanasi-78246"
link2 = "https://www.swiggy.com/restaurants/capsicum-lanka-varanasi-88160"

res = requests.get(link2)

soup = BeautifulSoup(res.text, 'html.parser')
res = soup.find_all('script')
dic = json.loads(str(res[3])[35:-9])
# print(dic)

# with open('capsicum.txt', 'w') as f:
#     f.write(str(res[4])[104:-(10 + 171 + 197 + 1637)])
data = json.loads(str(res[4])[104:-(10 + 171 + 197 + 1637)])


print(data['menu'].keys())
food_items = data['menu']['items']

for i in food_items:
    print(i)