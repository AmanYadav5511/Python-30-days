def sum_list(numbers):
    total = 0
    for i in numbers:
        total += i
    return total


print(sum_list([1,2,3,4,5]))
print(sum_list([]))