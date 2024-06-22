def make_readable(seconds):
    if seconds > 359999:
        return False
    
    hours = seconds // 3600
    minutesSeconds = seconds - hours * 3600 
    minutes = minutesSeconds // 60
    SecondsLeft = minutesSeconds - minutes * 60
    FinalResult = ('{:02}:{:02}:{:02}'.format(hours, minutes, SecondsLeft ))
    return FinalResult

print(make_readable(389000000))
 