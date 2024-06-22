def to_camel_case(text):
    if len(text) > 0:
        vartext = ''
        text = text.replace('-', ' ')
        text = text.replace('_', ' ')
        if text[0].isupper() == True:
            text = text.title()
            text = text.split()
            for value in text:
                vartext += value
            return vartext
        
        else:
            text = text.title()
            text = text.split()
            for pos, value in enumerate(text):
                if pos == 0:
                    value = value.lower()
                    vartext += value

                else:
                    vartext += value 
            return vartext
    else:
        return ''

to_camel_case('')