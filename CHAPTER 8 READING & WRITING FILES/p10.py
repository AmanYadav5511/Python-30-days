#count_lines(filename) — returns how many 
# lines are in a file, without loading the whole thing into a list first (loop and count).

def count_lines(filename):
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            count += 1
        print(count)
    
count_lines('log.txt')

