#Before writing a new invoice file, a script must never silently overwrite an existing one. 
#Write safe_write(filename, content) that checks os.path.exists() first 
#and refuses (prints a warning) if the file is already there.
import os
def safe_write(filename, content):
    if os.path.exists(filename):
       print("Warning file already exist!!")

    else:
        with open(filename, 'w') as f:
            f.write(content)
        print("File created succesfully!")

safe_write("long.txt", "New invoice")