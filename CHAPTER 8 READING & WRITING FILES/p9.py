#Read the same file three ways: .read() (whole file as one string), .readlines() (list of lines), 
# and looping for line in f directly. Print the type returned by each.

with open('log.txt', 'r') as f:
    data = f.read()
    print(data)
    print(type(data))

with open('log.txt', 'r') as f:
    data = f.readlines()
    print(data)
    print(type(data))

with open('log.txt', 'r') as f:
    for line in f:
        print(line.strip())
        print(type(line))