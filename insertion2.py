import numpy as np 

arr = np.array([[1,2],[3,4],[5,6],[55,77]])
new_arr = np.insert(arr, 1, [34,67] ,axis = None)
new_arr1 = np.insert(arr, 1, [34,67] ,axis = 0)
new_arr2 = np.insert(arr, 1, [34,7,9,4] ,axis = 1)

print(new_arr)
print(new_arr1)
print(new_arr2)
