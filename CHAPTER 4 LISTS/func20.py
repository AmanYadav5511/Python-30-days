def count_evens_odds(numbers):
    evens = 0
    odds = 0
    
    for num in numbers:
        if num % 2 == 0:
            evens += 1
            
        else:
            odds += 1
           
    return evens , odds

list = [1,2,3,4,5,6,7]
even_count,odd_count = count_evens_odds(list)
print(f"Even no are:{even_count}")
print(f"Odd no are: {odd_count}")
