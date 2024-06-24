from collections import Counter

def find_uniq(arr):
    x = Counter(arr)
    for number, amount in x.items():
        if amount == 1:
            return number
          
