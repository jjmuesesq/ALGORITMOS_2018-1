import sys

def merge(A, start, mid, end):
    p=start
    q= mid+1
    Arr=[0]*(end-start+1)
    k=0
    #print(range(start, end))
    for i in range(start, end+1):
        if(p > mid):
           Arr[k]=A[q]
           k+=1
           q+=1
           #print("if1")
        elif(q > end):
            Arr[k]=A[p]
            k+=1
            p+=1
            #print("if2")
        elif(A[p] < A[q]):
            Arr[k] = A[p]
            k+=1
            p+=1
            #print("if3")
        else:
            Arr[k]=A[q]
            k+=1
            q+=1
            #print("else")
        #print(Arr)
    for j in range(0, k):
        A[start] = Arr[j]
        start+=1
    return A


def merge_Sort(A, start, end):
    #print(A)
    if(start < end):
        mid= int((start+end)/2)
        merge_Sort(A, start, mid)
        merge_Sort(A, mid+1, end)
        merge(A, start, mid, end)

def my_print(lista):
    temp = ""
    for i in range(len(lista)):
        if (i != len(lista)):
            temp += (str(lista[i]) + " ")
        else:
            temp += (str(lista[i]))

    print(temp)
'''
M=[9, 7, 8, 3, 2, 1]
merge_Sort(M, 0, 5)
print(M)'''

T= int(input())
for k in range(T):
    a, b = map(int, input().strip().split(' '))
    #print(a, b)
    fil1 = list(map(int, input().strip().split(' ')))
    fil2 = list(map(int, input().strip().split(' ')))
    lista = fil1+fil2
    #print(len(lista))
    merge_Sort(lista, 0, len(lista)-1)
    my_print(lista[::-1])

'''
1
4 5
9 7 5 3
8 6 4 2 0
'''