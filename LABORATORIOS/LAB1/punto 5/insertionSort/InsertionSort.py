import sys

def insertionSort(A, N):
    B = A[:]
    #print(B)
    for i in range(N):
        # print(i)
        temp = A[i]
        j = i
        while (j > 0 and temp < A[j - 1]):
            A[j] = A[j - 1]
            j = j - 1
        A[j] = temp
    for t in range(N):
        for s in range(N):
            if(B[t]==A[s]):
                B[t]=s+1
                break



        # print([])
    return B


def my_print(lista):
    temp = ""
    for i in range(len(lista)):
        if (i != len(lista)):
            temp += (str(lista[i]) + " ")
        else:
            temp += (str(lista[i]))

    print(temp)


'''
M=[7, 4, 5, 2]
print(insertionSort(M, 4))
'''
T = int(input())
L = list(map(int, sys.stdin.readline().strip().split()))
# print(type(insertionSort(L,T)))
my_print(insertionSort(L, T))

'''
5
1 2 3 4 5

6
7 4 5 2 9 1

4 
7 5 4 2

50
66 83 29 26 12 3 90 6 68 28 82 58 9 21 22 39 52 1 70 31 15 99 94 50 20 77 48 76 5 87 67 78 69 49 63 57 96 43 79 97 18 100 92 91 14 80 46 61 33 74
29 41 15 13 6 2 43 4 31 14 40 26 5 11 12 18 24 1 33 16 8 49 46 23 10 36 21 35 3 42 30 37 32 22 28 25 47 19 38 48 9 50 45 44 7 39 20 27 17 34
'''