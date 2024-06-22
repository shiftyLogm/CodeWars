def cakes(recipe, available):
    recipeKeys = list(recipe.keys())
    recipeValues = list(recipe.values())
    availableKeys = list(available.keys())
    availableValues = list(available.values())
    realAvailableKeys = []
    realAvailableValues = []
    dictavailable = {}
    dictrecipe = {}

    if len(recipeKeys) > len(availableKeys):
        return 0

    else:
        index = 0   
        for key in recipeKeys:
            index = 0 
            while True:
                if index == len(availableKeys):
                    break

                if key == availableKeys[index]:
                    realAvailableKeys.append(key)
                    realAvailableValues.append(availableValues[availableKeys.index(key)])
                    break

                else:
                    index += 1
            
    if len(recipeKeys) > len(realAvailableKeys):
        return 0

    for pos, item in enumerate(recipeKeys):
        dictrecipe[item] = recipeValues[pos]

    for pos, item in enumerate(realAvailableKeys):
        dictavailable[item] = realAvailableValues[pos]   
    
    listdiv = []
    for pos in range(0, len(recipeValues)):
        listdiv.append(realAvailableValues[pos] // recipeValues[pos])

    return min(listdiv)