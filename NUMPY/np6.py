import numpy as np
arr = np.array([1,2,3,4])
newarr = arr.copy()
arr[0] = 42
print(arr)
print(newarr)