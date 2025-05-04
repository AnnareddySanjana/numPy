import numpy as np
arr = np.array([1,2,3,4,np.inf, 5,-np.inf])
print(np.isinf(arr))

aftercleaning = np.nan_to_num(arr, posinf = 200, neginf= -20)
print(aftercleaning)


