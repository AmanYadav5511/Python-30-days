def is_leap_year(year):
    if year % 400 == 0:
       return('its a leap year')

    if year % 100 == 0:
        return('not a leap year')

    elif year % 4 == 0:
        return('its a leap year')

    else:
        return('not a leap year')
    
print(is_leap_year(1900))