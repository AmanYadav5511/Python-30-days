def list_info(lst):
    
    if len(lst) == 0:
        print('It is a empty list')
    else:
        print('Length of list is ',len(lst))
        print('First item of list is ',  lst[0])
        print('Last item of list is ' , lst[-1])

spam = [10,20,30,40,50,60]
list_info(spam)
list_info([])