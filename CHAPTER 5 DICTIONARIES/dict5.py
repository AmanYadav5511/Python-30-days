def delete_key(d, key):
     print('Before ', d)

     if key in d:
        del d[key]
        print('The user wants to delete ' + key)
        print(key + ' deleted successfully')
     else:
         print('No key found with name '+ key + ' so can not delete')

     print('After ', d)

student = {'name':'aman','age':22,'city': 'Delhi','Age': 21}
delete_key(student,'name')
