#Reading exhausts the pointer — this bites real scripts.
#Open a file, call .read(), then call .read() again immediately. 
#What's in the second result? Fix it properly with .seek(0).

with open('notes.txt', 'r') as f:
    files = f.read()
    print(files)
    
    f.seek(0)
   
    filesss= f.read()
    print(filesss)
