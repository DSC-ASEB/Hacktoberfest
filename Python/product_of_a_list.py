
# A Python program to find a product of a list
# Author: Saketh-Chandra
# We can do this in two ways.

# 1st using Iteration
lst = [10, 5, 16, 23, 54, 6]
product = 1
for i in lst:
    product = product * i
print(product)  # Output 5961600

# 2nd using NumPy
import numpy as np

product = np.prod(lst)
print(product)  # Output 5961600
