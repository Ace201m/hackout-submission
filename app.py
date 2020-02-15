#!/home/khush/.local/share/virtualenvs/hackout-submission-KUwmPiwG/bin/python
from flask import Flask, jsonify, request
import re
import random
import os
import pickle
import sys

app = Flask(__name__)

@app.route('/recommender', methods=['GET'])
def get_tasks():
    filters = request.args['query']
    filters = re.sub('_', ' ', filters)
    filters = filters.split('*')

    if len(filters[0])==0:
        filters = []
    isveg = request.args['isveg']
    
    with open('./food_dataset.pkl', 'rb') as f:
        all_foods = pickle.load(f)

    if len(isveg)==0:
        data = {'options':['veg', 'both', 'nonveg']}
    else:
        print(filters)
        if isveg=='veg':
            a = 1
        elif isveg=='both':
            a = 2
        else:
            a = 3
        print(a)

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
                found = 0
                for category in filters:
                    if category in items.getCategory():
                        found+=1
                if found == len(filters):
                    res.append(items)

        print(len(res))
        if len(res)<=10:
            data = {'result':[]}
            for items in res:
                data['result'].append([str(items), items.getImage()])

            jsdata = jsonify(data)
            jsdata.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
            jsdata.headers['Access-Control-Allow-Credentials'] = True
            return jsdata

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
    jsdata = jsonify(data)
    jsdata.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    jsdata.headers['Access-Control-Allow-Credentials'] = True
    return jsdata

if __name__ == '__main__':
    app.run(debug=True)
