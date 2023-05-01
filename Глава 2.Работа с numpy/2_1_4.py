import numpy as np

Matrix = np.array([[5, 4], [2, -6]])
Vector = np.array([14, -2])            
REZ = np.linalg.solve(Matrix,Vector)
print(REZ)