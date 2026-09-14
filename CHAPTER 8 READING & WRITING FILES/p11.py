#A client sends you a notes.txt with trailing newlines on every line. 
# Write clean_lines(filename) that reads it and returns each line with .strip() applied, 
# so no \n characters remain.

def clean_lines(filename):
    with open(filename, 'r') as f:
       lines = f.read()
       print(lines.strip())

clean_lines('notes.txt')