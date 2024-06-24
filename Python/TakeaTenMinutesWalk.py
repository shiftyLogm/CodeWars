def is_valid_walk(walk):
    way = walk[:]

    if len(way) != 10:
        return False
    
    else:
        if way.count('n') == way.count('s') and way.count('w') == way.count('e'):
            return True
        
        else:
            return False
