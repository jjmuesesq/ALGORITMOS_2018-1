import sys

n=int(input())
ar=[]
for i in range(n):
    ar=[input()]
    for i in range(n):
        cnt=0
        for j in range(i):
            if ar[j]<ar[i]:
                cnt+=1
print(cnt)