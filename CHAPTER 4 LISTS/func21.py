def safe_double(numbers):  
  doubled_no = []
  for x in numbers:
    doubled_value = x*2
    doubled_no.append(doubled_value)
  return doubled_no
  

numbers = [1,2,3,4,5]
result = safe_double(numbers)
print(numbers)
print('after doubling....')
print(result)

