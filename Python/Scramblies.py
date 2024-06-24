def scramble(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    if s2 == '':
        return True

    for char in s2:
        if char not in s1:
            return False
        
    listEqual = []
    for char in s2:
        if char not in listEqual:
            if s2.count(char) > s1.count(char):
                return False
        listEqual.append(char)
                
    return True
        
    
print(scramble('kaates', 'steaak'))