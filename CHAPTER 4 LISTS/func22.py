import copy
nested = [[1, 2], [3, 4]]
shallow = copy.copy(nested)
deep = copy.deepcopy(nested)
nested[0][0] = 99
print(f"nested:  {nested}")
print(f"shallow: {shallow}")
print(f"deep:    {deep}")

# in deepcopy changes made to orignal doesn't affect deepcopy , its independent
# copy makes a copy of orignal list and changes made in orignal affects copy also