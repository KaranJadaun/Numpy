# Importing numpy library
import numpy as np

# Let a be an 2 x 2 array
a = np.array([(2,4),(3,4)], dtype = int)

# let b be an 2 x 2 array
b = np.array([(5,6),(2,6)], dtype = int)

print(a==b)
# Element wise comparision
# Output : [[False False]
#          [False False]]

print(a<3)
# Element wise comparision
# Output : [[ True False]
#           [False False]]

print(np.array_equal(a,b))
# Array wise comparision
# Output : False

# Thank you
