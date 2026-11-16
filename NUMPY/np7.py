import numpy as np
arr = np.array([1,2,3,4])
newarr = arr.view()
newarr[0] = 31
print(arr)
print(newarr)