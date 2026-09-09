import re
phonenumregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phonenumregex.search('My number is 415-555-4242')
print('Phone number found = ' + mo.group())