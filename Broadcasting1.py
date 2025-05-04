import numpy as np 

arr = np.array([10,20,30,40])
discount = 20
finalPrice = arr - (arr * discount/100)

print(finalPrice)
