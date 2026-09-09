import re
batRegex = re.compile(r'Bat(man|mobile|car|train)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))