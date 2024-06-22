def format_duration(seconds):

    year = seconds // 31536000
    monthSeconds = seconds - year * 31536000
    month = monthSeconds // 2592000
    daySeconds = seconds - month * 2592000
    day = daySeconds // 86400

    print(year, month, day)
format_duration(100000000)