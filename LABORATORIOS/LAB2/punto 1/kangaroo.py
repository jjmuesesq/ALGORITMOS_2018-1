"""
@author: Jhon Jairo
"""
import sys

def kangaroo(x1, v1, x2, v2):
    if((x1>x2 and v1>v2) or (x1<x2 and v1<v2) or (v1-v2)==0):
        return "NO"
    if((x1 - x2) % (v2 - v1)) == 0:
        return "YES"
    else:
        return "NO"

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)

'''
0 3 4 2
0 2 5 3

'''