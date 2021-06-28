# Importing numpy library
import numpy as np

print(np.zeros((3,4)))
# Create an array of zeros
# Output : [[0. 0. 0. 0.]
#           [0. 0. 0. 0.]
#           [0. 0. 0. 0.]]

print(np.ones((2,3,4)))
# Create an array of ones
# Output : [[[1. 1. 1. 1.]
#           [1. 1. 1. 1.]
#           [1. 1. 1. 1.]]

#          [[1. 1. 1. 1.]
#          [1. 1. 1. 1.]
#          [1. 1. 1. 1.]]]

print(np.arange(10,25,5))
# Create an array of evenly spaced values (step value)
# Output : [10 15 20]

print(np.linspace(0,2,9))
# Create an array of evenly spaced values ( number of spaces)
# Output : [0.   0.25 0.5  0.75 1.   1.25 1.5  1.75 2.  ]

print(np.full((2,2),7))
# Create an array of constant values
# Output : [[7 7]
#          [7 7]]

print(np.eye(4))
# Create an array of constant x contant identity matrix
# Output : [[1. 0. 0. 0.]
#           [0. 1. 0. 0.]
#           [0. 0. 1. 0.]
#           [0. 0. 0. 1.]]

print(np.random.random((3,3)))
# Create an array with random values
# Output : [[0.59031982 0.72602771 0.91437278]
#           [0.9487102  0.33680133 0.78380694]
#           [0.17365126 0.70957126 0.8236206 ]]

print(np.empty((3,2)))
# Create an empty array
# Output : [[1.70834462e-316 0.00000000e+000]
#           [6.89980051e-310 6.89978989e-310]
#           [6.89980041e-310 6.89978989e-310]]

# Thank you
