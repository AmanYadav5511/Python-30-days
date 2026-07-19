#Print the multiplication table of 
#7 from 7×1 to 7×10 using for + range(), formatted like 7 x 3 = 21.
number = 7
for i in range (1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")