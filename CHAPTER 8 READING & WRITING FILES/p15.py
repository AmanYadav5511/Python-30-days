#A vendor's export tool sometimes generates a completely empty file.
#Write is_empty_file(filename) that returns True/False without reading the 
#whole file (hint: os.path.getsize()).

import os
def is_empty_file(filename):
        if os.path.getsize(filename) == 0:
          print('empty file')
        else:
           print(os.path.getsize(filename))

is_empty_file('filecheck.txt')