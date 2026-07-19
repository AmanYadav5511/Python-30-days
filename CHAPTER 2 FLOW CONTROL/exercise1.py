#Take a variable age. Print "child" if under 13, "teenager" if 13–19, 
# "adult" if 20–59, "senior" if 60+. Test with edge values: 12, 13, 19, 20, 59, 60.

print('what is your age?')
age = int(input())
if age < 13 :
  print('You are a child.')
elif (age >= 13) and (age <= 19):
  print('You are a teenager')
elif (age >= 20) and (age <= 59):
  print('you are a adult')
else:
  print('You are a senior')
