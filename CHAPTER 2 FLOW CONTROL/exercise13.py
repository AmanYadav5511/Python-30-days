#Print 1 to 40. Multiples of 4 → "Ping", multiples of 6 → "Pong", multiples of both → "PingPong", 
#everything else → the number.

for num in range(1, 41):
    if num % 4 == 0 and num % 6 == 0:

       print(num , 'PingPong')
    
    elif num % 4 == 0:
       print(num , 'Ping')

    elif num % 6 == 0:
       print(num , 'Pong')

    else:
       print(num)