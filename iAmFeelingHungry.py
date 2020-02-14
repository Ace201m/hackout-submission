import pickle
f = open('food_dataset.pkl','rb')
a = pickle.load(f)
from Recommender import recommend
recommend(a)