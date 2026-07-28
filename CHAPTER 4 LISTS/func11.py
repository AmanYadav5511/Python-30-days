def sort_names(names):
    print(names)
    print('After sorting.....')
    print('---------------------')
    names.sort(key=str.lower)
    print('we get sorted list.....')
    print(names)

names = ['zara','Aman','bhavya','Chandan']
sort_names(names)