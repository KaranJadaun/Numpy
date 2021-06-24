# Importing numpy library
import numpy as np

# Creating a 3 dimensional array for understanding methods
a = np.array([[(1,2,3),(4,5,6),(7,8,9)],[(11,12,13),(14,15,16),(17,18,19)]],dtype=int)

print(a.shape)
# Array Dimensions
# Output : (2,3,3)
# which means it has 2 planes, 3 rows and 3 columns

print(len(a))
# Length of Array
# Output : 2
# which means it has 2 elements which are basically planes

print(a.ndim)
# Number of Array Dimensions
# Output : 3
# which means it is an 3 dimensional array

print(a.size)
# Number of Array elements
# Output : 18
# which means it has a total of 18 elements

print(a.dtype)
# Data Type of array elements
# Output : int64
# which means its an integer which occupies 64 bits of space

print(a.dtype.name)
# Name of Data Type
# Output : int64
# which means its an integer which occupies 64 bits of space

print(a.astype(float))
# Convert an array to a different data Type
# Output : [[[1. 2. 3. ]
#           [4. 5. 6. ]
#           [7. 8. 9. ]] 
#
#           [[11. 12. 13. ]
#            [14. 15. 16. ]
#            [17. 18. 19. ]]]

# Thank you
