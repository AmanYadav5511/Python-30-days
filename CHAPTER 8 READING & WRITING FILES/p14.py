#read_config(filename) — tries to open a config file and returns its contents.
#If the file doesn't exist, 
#catch FileNotFoundError and return a sensible default dict instead of crashing.

def read_config(filename):
    try:
        with open(filename, 'r') as f:
           readFile = f.read()
        print(readFile)
    except FileNotFoundError:
        print('Config file not found')
          
read_config("aman.config")