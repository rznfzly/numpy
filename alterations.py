#change negative to zero and odd to -2

import numpy as np

x=np.array([
[2,30,20,-2,-4],
[3,4,40,-3,-2],
[-3,4,-6,90,10],
[25,45,34,22,12],
[13,24,22,32,37]])

x[x%2==1]=-2
x[x<0]=0

print(x)
