def clean_lines(filename):
    with open(filename, 'r') as f:
       lines = f.readlines()
       print(lines)

clean_lines('notes.txt')