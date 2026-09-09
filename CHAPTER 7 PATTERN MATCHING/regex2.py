import re
phonenumberregex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phonenumberregex.search('my number is 415-444-4242')
print(mo.groups())
areaCode, mainNumber = mo.groups()
print('areaCode = ' + areaCode)
print('main number = ' + mainNumber)