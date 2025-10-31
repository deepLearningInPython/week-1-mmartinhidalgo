for name in dir():
    if not name.startswith(""):
        del globals()[name]

import numpy

# Follow the tasks below to practice basic Python concepts.
# Write your code in between the dashed lines.
# Don't import additional packages. Numpy suffices.

# Task 1: 
# Instructions:
#Write a function that takes one numeric argument as input. 
#If the number is larger than zero, the function should return 1, otherwise is should return -1.
#The name of the function should be step

# Your code here:
# -----------------------------------------------

def step(x):
  one_numeric = x
  if one_numeric > 0:
    return 1
  if one_numeric < 0 or one_numeric == 0:
    return -1

step(5)
step(-3)
step(0)

# -----------------------------------------------

# Task 2:
# Instructions:
#Write a function that takes in two arguments: a numpy array, and an integer (call argument "cutoff" and set default to 0).
#The function should return a numpy array of the same length, with all elements smaller than the cutoff being set to cutoff).
#The name of the function should be ReLu

# Your code here:
# -----------------------------------------------

def ReLu(a: numpy.array, cutoff = int(0)):
  return numpy.maximum(a, cutoff)

ReLu([-5, 0, 3, -2, 4])
ReLu([-5, 0, 3, -2, 4], cutoff = 2)
ReLu([])
  
# -----------------------------------------------

# Task 3:
# Instructions:
#Write a function that takes in a two-dimensional numpy array of size (n, p) and a one-dimensional numpy array of size p.
#The function should start by multiplying the two numpy arrays (matrix multiplication).
#Next, apply the ReLu function from above to the resulting matrix and return the result.
#Name the function neural_net_layer

# Your code here:
# -----------------------------------------------

def neural_net_layer(a: numpy.array, b: numpy.array):
  mult = a @ b
  return ReLu(mult)
    
inputs1 = numpy.array([[1, 2], [3, 4]])
weights1 = numpy.array([1, -1])

inputs2 = numpy.array([[2, 3], [1, 1]])
weights2 = numpy.array([1, 2])

inputs3 = numpy.array([[1, -1], [-2, 3]])
weights3 = numpy.array([-2, 1])

neural_net_layer(inputs1, weights1)
neural_net_layer(inputs2, weights2)
neural_net_layer(inputs3, weights3)

# ------------------------------------------
