import numpy as np

q = np.array([[2,8], [1,-6]])
w = np.array([[3,2,7],[4,1,8],[6,3,7]])
e = np.array([[4,3,2,7], [6,1,1,-2], [7,5,8,1],[9,5,-3,-5]])

Trans_q = q.transpose()
Trans_w = w.transpose()
Trans_e = e.transpose()
print('Транспонированные матрицы:')
print(Trans_q)
print(Trans_w)
print(TTrans_e)

Obrat_q = np.linalg.inv(q)
Obrat_w = np.linalg.inv(w)
Obrat_e = np.linalg.inv(e)
print('Обратные матрицы:')
print(Obrat_q)
print(Obrat_w)
print(Obrat_e)

Opred_q = np.linalg.det(q)
Opred_w = np.linalg.det(w)
Opred_e = np.linalg.det(e)
print('Определитель матриц:')
print(Opred_q)
print(Opred_w)
print(Opred_e)

Norm_w = np.linalg.norm(w,3,axis=1)
print('Норма векторов из строк матрицы 3x3:')
print(Norm_w)

Norm_e = np.linalg.norm(e,4,axis=0)
print('Норма векторов из столбцов матрицы 4x4:')
print(N_C)
