# count digits in number

print('Enter a number')
number = int(input())
count = 0
if number == 0:
    count = 1
while number > 0:
    number = number // 10
    count += 1
print(f"The number of digits are : {count}")