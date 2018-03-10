"""
@author: Jairo
"""
import time
import sys
start_time = time.time()

# INICIALIZAR MATRIZ DE (nxm)
def inicializar_mtx(n, m):
    tmp = []    
    for i in range (n):
        tmp.append([0]*(m))    
    return tmp

# IMPRIMIR UNA MATRIZ
def print_mtx(m):
    for i in range(len(m)):
        print(m[i])

# MULTIPLICA DOS MATRICES DE (nxm)
def mul_mtx(m1, m2):

    # SE VERIFICA SI SE PUEDEN MULTIPLICAR
    # LAS MATRICES
    if(len(m1) != len(m2[0])):
        print("NO SE PUEDEN MULTIPLICAR")
        return [[1]]
    else:        
        resultado = inicializar_mtx(len(m1), len(m2[0]))
        
        for i in range (len(m1)):
            for k in range (len(m2[0])):
                for j in range (len(m2)):
                    resultado[i][k] += (m1[i][j]*m2[j][k])
                #print("-->", i, "--",k)
                #print("##########")
        return resultado
        #print_mtx(resultado)

# =============================================
print("==================================")
print("MATRICES DE (nxn)")
print("==================================")
print("Ingrese dimensión de la Matriz A: ")
a = int(input())
A=[]
for i in range(a):
        fil = list(map(int, input().strip().split(' ')))
        A.append(fil)
print_mtx(A)
print("==================================")
print("Ingrese dimensión de la Matriz B: ")
b = int(input())
B=[]
for j in range(b):
        fil = list(map(int, input().strip().split(' ')))
        B.append(fil)
print_mtx(B)

print("==================================")
print("Resultado Multiplicación: ")
print_mtx(mul_mtx(A, B))
print("--- %s seconds ---" % (time.time() - start_time))

'''
1 2 3 4 5 6 7 8 9 3
8 7 6 5 4 2 1 3 4 5
0 4 5 7 1 2 3 4 8 6 
2 3 4 5 1 2 3 5 6 2
1 1 3 4 6 9 7 0 4 5
1 2 2 2 4 2 5 7 1 2
8 7 6 5 4 3 2 1 8 9
7 2 5 6 3 2 1 4 5 6
1 2 3 4 5 1 2 3 4 5
8 7 3 2 1 1 1 3 6 4

1 2 3 4 5 6 7 8 9 1
8 7 6 5 4 2 1 3 4 1
0 4 5 7 1 2 3 4 8 1 
2 3 4 5 1 2 3 5 6 1
1 1 3 4 1 2 3 0 4 1
1 2 2 2 4 2 5 7 1 6
8 7 6 5 4 3 2 1 8 1
7 2 5 6 3 2 1 4 4 4
1 2 3 4 5 1 2 3 4 3
8 7 3 2 0 1 1 1 6 8
'''
