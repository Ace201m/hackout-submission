import re

class Food:

    def __init__(self, food_dict, rest_name, rest_image):
        self.name = food_dict['name']
        self.price = food_dict['price']/100
        self.isveg = food_dict['isVeg']
        self.only_category = food_dict['category']
        self.category = (self.only_category + ' ' + self.name).lower()
        self.cleanCategory()
        self.description = food_dict['description']
        self.rest = rest_name
        self.rest_image = rest_image

    def getImage(self):
        return self.rest_image
    
    def getName(self):
        return self.name

    def cleanCategory(self):

        cats = []
        for word in self.category.split():
            if word.isalpha():
                cats.append(word)
        self.category = ' '.join(cats)

        self.category = re.sub(r'&#39', '\'', self.category)
        self.category = re.sub(r'[^0-9a-zA-Z ]+', '', self.category).split()

        together_cats = ['main course', 'do pyaza']
        self.category = '#'.join(self.category)
        
        for items in together_cats:
            temp_item = re.sub(' ', '#', items)
            if temp_item in self.category:

                self.category = re.sub(temp_item, items, self.category)

        self.category = self.category.split('#')


    def getCategory(self):
        return self.category

    def getIsVeg(self):
        return self.isveg

    def __str__(self):
        return self.name + ', from-'+self.rest