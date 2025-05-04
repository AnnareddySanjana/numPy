import numpy as np
arr = np.array([1,2,3,4,np.nan])
print(np.isnan(arr))

aftercleaning = np.nan_to_num(arr)
print(aftercleaning)

aftercleaning2 = np.nan_to_num(arr, nan=90)
print(aftercleaning2)
