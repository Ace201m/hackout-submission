import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/cuisine"

payload = "ingredientList=butter%20chicken"
headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "7abc5c4f52mshcfc10264afc7226p1c5047jsne5a0053cb873",
    'content-type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)