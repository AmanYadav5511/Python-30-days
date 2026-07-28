def comma_code(mylist):
    result = ''
    for i in range(len(mylist)):
        if i == len(mylist) - 1:
            result = result + 'and ' + mylist[i]
        else:
            result = result + mylist[i] + ', '
    return result

spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(spam))