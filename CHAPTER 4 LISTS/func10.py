def find_position(lst, item):
    try:
        return 'Item is at index = ', lst.index(item)
        
    except ValueError:
        return 'item not in list'
    
spam = ['aman','car','bat','hat','light']
print(find_position(spam,'light'))