class Food:

    def __init__(self, food_dict, rest_name):
        self.name = food_dict['name']
        self.price = food_dict['price']/100
        self.isveg = food_dict['isVeg']
        self.category = food_dict['category']+' '+food_dict['name']
        self.category = self.category.split(' ')
        self.description = food_dict['description']
        self.rest = rest_name
    
    def getName(self):
        return self.name

    def getCategory(self):
        return self.category

    def __str__(self):
        return self.name 