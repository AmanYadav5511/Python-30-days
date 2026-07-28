def add_to_end(lst, item):
    print('Before add to end : ',lst)
    lst.append(item)
    print('after add to end : ',lst)
def add_to_start(lst, item):
    print('after add to start : ',lst)
    lst.insert(0,item)
    print('after add to start : ',lst)

new = ['aman']
add_to_end(new, 'hello')
add_to_start(new, 'bye')