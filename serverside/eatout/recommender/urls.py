from django.urls import path

from .views import *

app_name = 'recommender'
urlpatterns = [
    path('', index , name='index'),
]