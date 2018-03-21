"""
@author: Jhon Jairo
"""
import math
import random
import itertools
from itertools import permutations
from math import factorial

#tomado de notebooK corrección y analisis de algoritmos
def insertion_sort(A):
    j = 1
    while j < len(A):
        key = A[j]
        i = j - 1
        while (i >= 0) and (A[i] > key):
            A[i + 1] = A[i]
            i = i -1
        A[i + 1] = key
        j = j + 1
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

def isortSteps(a):
    v = []
    for i in range(len(a)):
        v.append(a[i])
        
    steps = 0
    for i in range(1,len(v)):
        x = v[i]
        j = i-1
        while (j > -1) and (v[j] > x):
            v[j+1] = v[j]
            j = j -1
            steps = steps + 3
        steps = steps + 1
        v[j+1] = x
        steps = steps + 4
    steps = steps + 1
    #print(a)
    return steps

#print(randomPerm(5))

print("---------------------------------------------------")
print("Programa en Python que ejecuta Insertion Sort sobre")
print("todas las permutaciones                            ")
print("Version usando: permutations de Itertools          ")
print("---------------------------------------------------")
print("Arreglo B: ", "\n")
B = [5, 4, 3, 2, 1]
print(B, "\n")
#insertion_sort(B)
#print (B, "\n")
print("Insertion sort sobre todas las permutaciones de un arreglo B \n")
print("tamaño de B: ", len(B), "\n")
print()

miLista=list(itertools.permutations(B, len(B)))

#print(type(miLista))
#tmp = list(miLista[0])
#print(type(tmp))

for i in range(len(miLista)):
    print(" permutacion ", i+1, miLista[i])
    print("lista ordenada ", insertion_sort(list(miLista[i])), "\n")


print("-----------------------------------------------------------")    
print("hasta que valor se pueden generar las permutaciones        ")
print("-----------------------------------------------------------")
print("Arreglo B: \n")
print(B, "\n")
print("El numero de permutaciones que se pueden obtener para un   ")
print("conjunto de cardinalidad n es n! \n")
if len(miLista)==factorial(len(B)):
    print("# n de permutaciones de B  igual n!")
else:
    print("false")


print("-----------------------------------------------------------")    
print("Insertion Sort sobre una muestra aleatoria de permutaciones")
print("-----------------------------------------------------------")
print("Arreglo B: \n")
print(B, "\n")
print("muestras aleatorias de permutaciones del arreglo B: \n")

n=len(B)
sum = 0
min = n**3
max = 0
for i in range(len(B)):
    A = randomPerm(len(B))
    print("(", i+1 ,")","permutacion aleatoria: ", A )
    #print("arreglo B ordenado: ", insertion_sort(A))
    t = isortSteps(A)
    print ("# pasos :", t)
    print("arreglo B ordenado: ", insertion_sort(A), "\n")
   
    if t < min :
       min = t
    if t > max :
       max = t
    sum = sum + t

print ('Theoretical best time, ' + str(5*n - 4)) 
print ('Theoretical worst time,' + str((3.0/2.0)*n**2 + (7.0/2.0)*n - 4))
print ('Theoretical average time,' + str((3.0/4.0)*n**2 + (17.0/4.0)*n - 4))
print ('Experimenal best time, ' + str(min))
print ('Experimenal worst time,' + str(max))
print ('Experimenal average time,' + str(sum/n))





