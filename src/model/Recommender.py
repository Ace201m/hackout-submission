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
            tempList.append[tempDict[a]]
        
        tempList.sort()
        tempList=tempList[-4:]

        selected
                


        # refine after selecting optin