'''
Created on 1 feb. 2016

@author: Timo
'''
priem = list(range(2,1001))
def findPriem(a):
    k=len(a)
    for i in range(0,k):
        if a[i] != 0:
            for c in range(0,k):
                if a[c] % a[i] == 0 and a[c] / a[i] != 1:
                    a[c] = 0;
    a.sort()
    zero = a.count(0)
    del a[:zero]
    return a
print(findPriem(priem)) 