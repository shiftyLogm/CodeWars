def pig_it(text):
    text = text.strip().split()

    final_string = ''
    for word in text:
        if word.isalpha():
            first_char = word[0]
            word = word.replace(first_char, '', 1)
            word = word + f'{first_char}ay'
        final_string += f'{word} ' 
    final_string = final_string.strip()

    return final_string


pig_it('Pig latin is cool')