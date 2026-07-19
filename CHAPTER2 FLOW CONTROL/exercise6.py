#Sum all even numbers from 1 to 100 using a loop (answer should be 2550). 
# Then do it again using only range()'s three arguments — start, stop, step.

total = 0
for num in range(0, 101 ,2):
    total = total + num
    print(total)