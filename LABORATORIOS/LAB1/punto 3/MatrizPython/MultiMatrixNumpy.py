import numpy as np
from time import time
import matplotlib.pyplot as plt

#multipliacion de matrices utilizando numpy
'''
A = np.array([[1, 2, 3, 12, 6],
             [4, 5, 6, 15, 20],
             [7, 8, 9, 10, 10]])
print(A)

B = np.array([[4, 4, 2],
             [2, 3, 1],
             [6, 5, 8],
             [9, 9, 9]])
print(B)

print(np.dot(B, A))'''
print("-----------------------------------")
print("ingrese la dimensión de la matriz A")
print("-----------------------------------")
mtxA = []
N = int(input())
for j in range(N):
    filA = list(map(int, input().strip().split(' ')))
    mtxA.append(filA)
A=np.array(mtxA)
print("A : ")
print(A)
print("-----------------------------------")
print("ingrese la dimensión de la matriz B")
print("-----------------------------------")
mtxB = []
T = int(input())
for i in range(T):
    filB = list(map(int, input().strip().split(' ')))
    mtxB.append(filB)
B=np.array(mtxB)
print("B : ")
print(B)
print("-----------------------------------")
print("Multiplicación de AxB")
print("-----------------------------------")
print(np.dot(A, B))