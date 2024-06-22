def DescNum(num):
    numdesc = ''
    num = str(num)
    listnum = []

    for algarismo in num:
        listnum.append(algarismo)

    listnum.sort(reverse=True)

    for algarismo in listnum:
        numdesc += algarismo
    
    return int(numdesc)

print(DescNum(421459321421))