# Importing numpy library
import numpy as np

# Creating a 1D array
print(np.array([1,2,3]))
# Output : [1 2 3]

# Creating a 2D array 
# dtype is used to define the data type of the numpy array
print(np.array([(1,2,3),(4,5,6)],dtype = int))
# Output : [[1 2 3] 
#           [4 5 6]]

# Creating a 3D array
# dtype for defining that the array is in float
print(np.array([[(1,2,3),(4,5,6),(7,8,9)],[(11,12,13),(14,15,16),(17,18,19)]],dtype=float))
# Output : [[[1. 2. 3. ]
#           [4. 5. 6. ]
#           [7. 8. 9. ]] 
#
#           [[11. 12. 13. ]
#            [14. 15. 16. ]
#            [17. 18. 19. ]]]

# Thank You
