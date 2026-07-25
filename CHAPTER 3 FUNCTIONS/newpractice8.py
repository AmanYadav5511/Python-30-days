def max(a,b,c):
   if (a >= b) and (a >= c):
      return('a is larger')

   elif (b >= a) and (b >= c):
      return('b is larger')

   elif (c >= a) and (c >= b):
      return('c is larger')
    
print(max(4,2,3))