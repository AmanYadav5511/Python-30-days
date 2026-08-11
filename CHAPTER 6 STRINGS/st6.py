def is_python_filename(spam):

    print(spam.startswith('script'))
    print(spam.endswith('.py'))
    print(car.endswith('.py'))

spam = 'script.py'
car = 'script.pyc'
is_python_filename(spam)