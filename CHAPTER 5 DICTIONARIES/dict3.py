def describe(d):
    count = 0
    for k in d.keys():
      count +=1
    print('This dictionary has total '+ str(count) + ' keys')
      

student = {'name':'aman','age':22,'city': 'Delhi','Age': 21}
describe(student)