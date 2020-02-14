


class Restaurent:

    def __init__(self, name, city, image, cuisine, rating, rating_count, locality, price_range):
        self.name = name
        self.city = city
        self.image = image
        self.cuisine = cuisine
        self.rating = rating
        self.rate_count = rating_count
        self.locality = locality
        self.price_range = price_range

    def __str__(self):
        return self.name + ", "+ self.locality + ", " + self.city
        