class Food:

    def __init__(self, food_dict, rest_name):
        self.name = food_dict['name']
        self.price = food_dict['price']
        self.isveg = food_dict['isVeg']
        self.category = food_dict['category']
        self.description = food_dict['description']
        self.rest = rest_name

    def __str__(self):
        return self.name 