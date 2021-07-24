import numpy as np
a=np.array([0,1,2])
b=np.array([2,1,0])
Cov_mat=np.cov(a,b)
print("la matrice est : ", Cov_mat)