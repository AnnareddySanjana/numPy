import numpy as np 

arr1 = np.array([1,2,3,4])
arr2 = np.array([7,4,9,2,2])
new_arr = np.concatenate((arr1,arr2))
print(new_arr)

arr3 = np.array([[2,3],[4,5]])
arr4 = np.array([[3,4],[5,6]])
New_arr=np.concatenate((arr3,arr4))
print(New_arr)
