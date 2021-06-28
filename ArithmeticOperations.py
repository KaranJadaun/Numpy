# Importing numpy library
import numpy as np

# Let a be an 2 x 2 array
a = np.array([(2,4),(3,4)], dtype = int)

# let b be an 2 x 2 array
b = np.array([(5,6),(2,6)], dtype = int)

print(a - b)
# Subtraction
# Output : [[-3 -2]
#           [ 1 -2]]

print(np.subtract(a,b))
# Subtraction
# Output : [[-3 -2]
#           [ 1 -2]]

print(a + b)
# Addition
# Output : [[ 7 10]
#          [ 5 10]]

print(np.add(a,b))
# Addition
# Output : [[ 7 10]
#          [ 5 10]]

print(a/b)
# Division
# Output : [[0.4        0.66666667]
#           [1.5        0.66666667]]

print(np.divide(a,b))
# Division
# Output : [[0.4        0.66666667]
#           [1.5        0.66666667]]

print(a*b)
# Multiplication
# Output : [[10 24]
#          [ 6 24]]

print(np.multiply(a,b))
# Multiplication
# Output : [[10 24]
#          [ 6 24]]

print(np.exp(a))
# Exponentiation
# Output : [[ 7.3890561  54.59815003]
#          [20.08553692 54.59815003]]

print(np.sqrt(a))
# Square root
# Output : [[1.41421356 2.        ]
#          [1.73205081 2.        ]]

print(np.sin(a))
# Sines of an array
# Output : [[ 0.90929743 -0.7568025 ]
#           [ 0.14112001 -0.7568025 ]]

print(np.cos(a))
# Cosines of an array 
# Output : [[-0.41614684 -0.65364362]
#           [-0.9899925  -0.65364362]]

print(np.log(a))
# Natural logarithm of an array 
# Output : [[0.69314718 1.38629436]
#           [1.09861229 1.38629436]]

print(a.dot(b))
# Dot-product
# Output : [[18 36]
#           [23 42]]

# Thank You
