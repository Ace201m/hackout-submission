## given foodlist, it gives me 4 options and i would select one of them till it gives me dishes

def recommend(foodlist):
    res = foodlist
    while(len(res)>10):
        # get options
        tempDict = {}
        for food in res:
            categoryList = food.getCategory()
            for category in categoryList:
                if category not in tempDict:
                    tempDict[category]=0
            tempDict[category] += 1
        
        tempList = []
        for a in tempDict:
            tempList.append(tempDict[a])
        
        tempList.sort()
        tempList=tempList[-5:]

        # select from optins
        print("Select option -")
        for i in range(len(tempList)):
            print(tempList[i],str(i))
        print("Give index of your selection")
        selected = str(input())

        selected = tempList[selected]

        # refine after selecting optin
        tempRes = []
        for food in res:
            if selected in food.getCategory():
                tempRes.append(food)
        res = tempRes
    print(res)