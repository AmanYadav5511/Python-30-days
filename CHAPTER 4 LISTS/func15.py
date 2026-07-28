def largest(numbers):
    largest = numbers[0]
    for n in numbers:
        if n > largest:
           largest = n
    return largest

numbers=[10,80,70,60]
print(largest(numbers))