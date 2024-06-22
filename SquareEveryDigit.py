def square_digits(num):
    listNum = map(int, (str(num))) 
    listNum = map(lambda n: n**2, listNum) # [4, 4]
    return int(''.join(map(str, listNum)))

print(square_digits(22))