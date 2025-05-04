import numpy as np 

pricelist = [100,200,300,400]

discount = 20

finalPrice = []

for price in pricelist:
  result = price - (price * discount/100)
  finalPrice.append(result)
  
print(finalPrice)
