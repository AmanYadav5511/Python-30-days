def reverse_list(lst):
    reversed_list = []
    for item in lst:
        reversed_list.insert(0, item)
    return reversed_list

lst = [10,20,30,40,50]
print(reverse_list(lst))