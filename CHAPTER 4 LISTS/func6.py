def contains(lst , item):
    return item in lst

def count_matches(lst, item):
    match_count = 0
    for element in lst:
        if element == item:
            match_count +=1
    return match_count

print(contains([10,20,20,20,20,30,40],20))
print(contains([10,20,20,20,20,20,30,40],50))
print(count_matches([10,20,20,20,20,30,40],20))