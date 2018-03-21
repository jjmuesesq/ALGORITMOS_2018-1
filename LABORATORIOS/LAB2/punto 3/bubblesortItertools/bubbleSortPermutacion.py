"""
@author: Jhon Jairo
"""
import math
import random
import itertools
from itertools import permutations
from math import factorial

def bubble_sort(A, n):
    temp = 0
    swap=0
    #print (A[1])
    for k in range(n-1):
        for i in range(n-k-1):
            #if(A[i]==A[i+1]):
                                
            if (A[i] > A[i+1]):
                #print (i)
                #print (A[i])
                #print ("prueba")
                #print(A[i+1])
                temp=A[i]
                A[i]=A[i+1]
                A[i+1]=temp
                swap=swap+1
    print("# swaps:", swap)
    return A

#basado en el codigo de insertionsortPermutacion.py
def randomPerm(n):
    v=[]
    for i in range(n):
        v.append(i+1)
    for i in range(len(v)-1):
        j = random.randint(i, len(v)-1)
        aux = v[i]
        v[i] = v[j]
        v[j] = aux
    return v

print("---------------------------------------------------")
print("Programa en Python que ejecuta Bubble Sort sobre")
print("todas las permutaciones                            ")
print("Version usando: permutations de Itertools          ")
print("---------------------------------------------------")
print("Arreglo B: ", "\n")
B = [5, 4, 3, 2, 1]
print(B, "\n")
print("Bubble sort sobre todas las permutaciones de un arreglo B \n")
print("tamaño de B: ", len(B), "\n")
print()

miLista=list(itertools.permutations(B, len(B)))

for i in range(len(miLista)):
    print(" permutacion ", i+1, miLista[i])
    print("lista ordenada ", bubble_sort(list(miLista[i]), len(B)), "\n")
    
print("-----------------------------------------------------------")    
print("hasta que valor se pueden generar las permutaciones        ")
print("-----------------------------------------------------------")
print("Arreglo B: \n")
print(B, "\n")
print("El numero de permutaciones que se pueden obtener para un   ")
print("conjunto de cardinalidad n es n! \n")

if len(miLista)==factorial(len(B)):
    print("# n de permutaciones de B  igual n! \n")
else:
    print("false")


print("-----------------------------------------------------------")    
print("Insertion Sort sobre una muestra aleatoria de permutaciones")
print("-----------------------------------------------------------")
print("Arreglo B: \n")
print(B, "\n")
print("muestras aleatorias de permutaciones del arreglo B: \n")

for i in range(len(B)):
    A = randomPerm(len(B))
    print("(", i+1 ,")","permutacion aleatoria: ", A )
    print("arreglo B ordenado: ", bubble_sort(A, len(B)), "\n")
