#replace last row with 0
import numpy as np
matrix=np.array([[2,30,20,-2,-4],[3,4,40,-3,-2],[-3,4,-6,90,10],[25,45,34,22,12],[13,24,22,32,37]])
matrix[4]=0
print(matrix)
