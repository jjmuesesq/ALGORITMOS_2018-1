import sys
import time

start_time = time.time()

#Solución Recursiva
def fibonacci0(n):
    if(n<=1):
        return 1
    else:
        return fibonacci0(n-1)+ fibonacci0(n-2)
    print(fibonacci0(4))

#Bottom-up 1 tabular solution
def fibonacci1(n):
    arrayFibo=[0, 1]
    for i in range(2, n+1):
        arrayFibo.append(arrayFibo[i-1]+arrayFibo[i-2])
    return arrayFibo[n]
    print(arrayFibo)

T=int(input())
print(fibonacci0(T))
print("--- %s seconds ---" % (time.time() - start_time))
#complejidad de fibonaci O(n) forma iterativa







