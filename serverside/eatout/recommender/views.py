from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

import pickle
import random
import re
import os


def index(request):
    filters = request.GET.get('query')
    filter = re.sub('#', ' ', filters)
    filters = filters.split('*')
    isveg = request.GET.get('isveg')
    path = os.path.dirname(__file__)
    filepath = os.path.join(path, 'food_dataset.pkl')

    print(filepath)
    with open(filepath, 'rb') as f:
        all_foods = pickle.load(f)

    if isveg is None:
        data = {'options':['veg', 'both', 'nonveg']}
    else:
        if isveg=='veg':
            a = 1
        elif isveg=='both':
            a = 2
        else:
            a = 3

        res = []
        if a!=2:
            if a==3:
                tempList = []
                for food in all_foods:
                    if food.getIsVeg()==0:
                        tempList.append(food)
            if a==1:
                tempList = []
                for food in all_foods:
                    if food.getIsVeg()==1:
                        tempList.append(food)
            all_foods = tempList

        for items in all_foods:
            for category in filters:
                if category in items.getCategory():
                    res.append(items)
                    break

        if len(res)<=10:
            data = {'result':[]}
            for items in res:
                data['result'].append(str(items))

        excep = ['',' ']
        excep.extend(filters)
        tempDict = {}
        for food in res:
            categoryList = food.getCategory()
            for category in categoryList:
                if category in excep:
                    continue
                if category not in tempDict:
                    tempDict[category]=0
                tempDict[category] += 1
        
        tempList = []
        for a in tempDict:
            tempList.append(tempDict[a])
        
        tempList.sort()
        tempList=tempList[-5:]

        tempTempList = []
        for category in tempDict:
            if tempDict[category] in tempList:
                tempTempList.append(category)

        tempList = tempTempList
        random.shuffle(tempList)
        # giving 4 options
        tempList = tempList[-4:]

        data = {'options':tempList}
    return JsonResponse(data)

def get404(request):
    return HttpResponse('this page is not created :(')