from bs4 import BeautifulSoup
import requests, json

link = "https://www.swiggy.com/restaurants/al-baik-world-ravindrapuri-lanka-varanasi-78246"
link2 = "https://www.swiggy.com/restaurants/capsicum-lanka-varanasi-88160"

res = requests.get(link2)

soup = BeautifulSoup(res.text, 'html.parser')
res = soup.find_all('script')
dic = json.loads(str(res[3])[35:-9])
print(dic)
print(str(res[4])[104:-10])