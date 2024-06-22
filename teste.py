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
                if index == len(recipeKeys):
                    break

                if key == availableKeys[index]:
                    realAvailableKeys.append(key)
                    realAvailableValues.append(availableValues[availableKeys.index(key)])
                    break

                else:
                    index += 1
            

        print(len(recipeKeys), len(realAvailableKeys))