import numpy as np 

arr1 = np.array([1,2])
arr2 = np.array([10,20])
new_arrv = np.vstack((arr1,arr2))
new_arrh = np.hstack((arr1,arr2))
print(new_arrv)
print(new_arrh)
