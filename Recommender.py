import random

## given foodlist, it gives me 4 options and i would select one of them till it gives me dishes

def recommend(foodlist):
    res = foodlist
    # ask for veg non veg
    print("Select preference")
    print("1 for only veg, 2 for both and 3 for only non veg")
    a = int(input())
    if a!=2:
        if a==3:
            tempList = []
            for food in res:
                if food.getIsVeg()==0:
                    tempList.append(food)
        if a==1:
            tempList = []
            for food in res:
                if food.getIsVeg()==1:
                    tempList.append(food)
        res = tempList
        
    excep = ['',' ']
    while(len(res)>10):
        # get options
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
        tempList = tempList[-6:]

        # select from optins
        print("Select option -")
        for i in range(len(tempList)):
            print(tempList[i],str(i))
        print("Give index of your selection")
        selected = int(input())

        selected = tempList[selected]
        excep.append(selected)

        # refine after selecting optin
        tempRes = []
        for food in res:
            if selected in food.getCategory():
                tempRes.append(food)
        res = tempRes
    for item in res:
        print(str(item))