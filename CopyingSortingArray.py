# Importing numpy library
import numpy as np

# Let a be an 2 x 2 array
a = np.array([(2,4),(3,4)], dtype = int)

# let b be an 2 x 2 array
b = np.array([(5,6),(2,6)], dtype = int)

c = a.view()
print(c)
# Create a view of the array with same data 
# Output : [[2 4]
#           [3 4]]

d = np.copy(a)
print(d)
# Create a copy of the array
# Output : [[2 4]
#           [3 4]]

e = a.copy()
print(e)
# Create a deep copy of the array
# Output : [[2 4]
#          [3 4]]

f = np.sort(a)
print(f)
# Sort an array
# Output : [[2 4]
#          [3 4]]

g = np.sort(b, axis=0)
print(g)
# Sort the elements of an array's axis
# Output : [[2 6]
#          [5 6]]

# Thank You
