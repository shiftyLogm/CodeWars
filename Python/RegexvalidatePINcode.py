def validate_pin(pin):
    if len(pin) != 4 and len(pin) != 6:
        return False
    
    elif pin.isnumeric() == True:
        return True
    
    else:
        return False