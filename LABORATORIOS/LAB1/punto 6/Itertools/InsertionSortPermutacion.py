"""
@author: Jhon Jairo
"""
import itertools
from itertools import permutations
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

print("Arreglo B: ", "\n")
B = [5, 7, 1, 3]
print(B, "\n")
#insertion_sort(B)
#print (B, "\n")
print("Insertion sort sobre todas las permutaciones de un arreglo B")
miLista=list(itertools.permutations(B, 4))

#print(type(miLista))
#tmp = list(miLista[0])
#print(type(tmp))

for i in range(len(miLista)):
    print(miLista[i])
    print(insertion_sort(list(miLista[i])), "\n")
    
    
