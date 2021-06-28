# Importing numpy library
import numpy as np

# Let a be an 2 x 2 array
a = np.array([(2,4),(3,4)], dtype = int)

# let b be an 2 x 2 array
b = np.array([(5,6),(2,6)], dtype = int)

print(a.sum())
# Array wise sum
# Output : 13

print(a.min())
# Array wise minimum value
# Output : 2

print(b.max(axis=0))
# Maximum value of an array row
# Output : [5 6]

print(b.cumsum(axis=0))
# Cumulative sum of the elements
# Output : [[ 5  6]
#          [ 7 12]]

print(a.mean())
# Mean
# Output : 3.25

print(np.std(b))
# Standard Deviation
# Output : 1.6393596310755

# Thank You 
