"""
@author: Jhon Jairo
"""

"""
@author: Jhon Jairo
"""
import itertools
from itertools import permutations
def bubble_sort(A, n):
    temp = 0
    #swap=0
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
                #swap=swap+1
    return A

print("Arreglo B: ", "\n")
B = [5, 7, 1, 3]
print(B, "\n")
n=len(B)
print(type(n))
#insertion_sort(B)
#print (B, "\n")
print("Bubble sort sobre todas las permutaciones de un arreglo B")
miLista=list(itertools.permutations(B, 4))

for i in range(len(miLista)):
    print(miLista[i])
    print(bubble_sort(list(miLista[i]), n), "\n")
    
    
