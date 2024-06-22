def generate_hashtag(s):
    if s == '':
        return False
    
    phrase = ''
    s = s.split()
    for word in s:
        word = word.capitalize()
        phrase += word
    
    phrase = ('#'+f'{phrase}')
    if len(phrase) > 140:
        return False
    
    else:
        return phrase


print(generate_hashtag('palavra papap papa'))