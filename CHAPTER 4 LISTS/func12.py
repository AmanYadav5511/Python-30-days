def sort_descending(numbers):
    numbers.reverse()  #.reverse() flips the original positions of the elements without looking at their values
    numbers.sort(reverse=True) # .sort(reverse=True) evaluates the values of the elements and arranges them in descending order
    print('The list in descendinf order will be -')
    print(numbers)

numbers = [10,30,20,50,40,60]
sort_descending(numbers)

