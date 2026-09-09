def isPhonenumber(text):
    if len(text) != 12:
        return False
    for i in range(0 , 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhonenumber(chunk):
       print('Phone number found: ' + chunk)
print('Done')




#Index (i)  | Chunk Extracted (12 chars) | Is Phone Number? | What Happens?
#-----------|----------------------------|------------------|-----------------------------
#i = 0      | 'Call me at '              | False            | Nothing printed.
#i = 1      | 'all me at 4'              | False            | Nothing printed.
#...        | ...                        | False            | ...
#i = 11     | '415-555-1011'             | TRUE!            | PRINTS: Phone number found: 415-555-1011
#i = 12     | '15-555-1011 '             | False            | Nothing printed.
#...        | ...                        | False            | ...
#i = 34     | '415-555-9999'             | TRUE!            | PRINTS: Phone number found: 415-555-9999
#i = 35     | '15-555-9999 '             | False            | Nothing printed.
#...        | ...                        | False            | ...
#i = 60     | '.'                        | False            | Loop finishes.