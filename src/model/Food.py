import re

class Food:

    def __init__(self, food_dict, rest_name):
        self.name = food_dict['name']
        self.price = food_dict['price']/100
        self.isveg = food_dict['isVeg']
        self.only_category = food_dict['category']
        self.category = (self.only_category + ' ' + self.name).lower()
        self.cleanCategory()
        self.description = food_dict['description']
        self.rest = rest_name
    
    def getName(self):
        return self.name

    def cleanCategory(self):

        cats = []
        for word in self.category.split():
            if word.isalpha():
                cats.append(word)
        self.category = ' '.join(cats)

        together_cats = ['main course']
        
        for items in together_cats:
            if self.only_category.strip().lower()==items:
                self.category = self.name.lower()
                self.category += ' ' + items
                break

        self.category = re.sub(r'[^0-9a-zA-Z ]+', '', self.category)
        self.category = re.sub(' +', ' ', self.category).split()

    def getCategory(self):
        return self.category

    def __str__(self):
        return self.name 