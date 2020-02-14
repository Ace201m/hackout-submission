class Food:

    def __init__(self, name, price, isveg, category, description, rest_list):
        self.name = name 
        self.price = price 
        self.isveg = isveg
        self.category = category
        self.description = description
        self.rest_list = rest_list

    def __str__(self):
        return self.name 