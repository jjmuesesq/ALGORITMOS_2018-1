
"""
@author: Jhon Jairo
"""

def misterio(n):
    if n <= 1:
        return 1
    else:
        r = misterio(n/2)
        i = 1
        while(n>(i*i)):
            i = i+1
        r= r + misterio(n/2)
        return r

print(misterio(0))
print(misterio(1))
print(misterio(2))
print(misterio(3))
print(misterio(4))