import numpy as np 

arr1 = np.array([1,3,4,5,6,2])

new_arr = np.split(arr1,2)
arrv = np.array([[1,2],[7,8]])
new_arrv = np.vsplit(arrv, 2)
new_arrh = np.hsplit(arrv, 2)
print(new_arr)
print(new_arrv)
print(new_arrh)

