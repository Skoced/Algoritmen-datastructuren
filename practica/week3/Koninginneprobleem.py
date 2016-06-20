'''
Created on 10 mrt. 2016

@author: Timo
'''
def check(a,i):
    n=len(a)
    return not ( i in a or i+n in [a[j]+j for j in range(n)] or i-n in [a[j]-j for j in range(n)])

def printQueens(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i]==j:
                print("X",end=" ")
            else:
                print("*",end=" ")
        print()
    print()

def rsearch(N):
    global a
    for i in range(N):
        if check(a,i):
            a.append(i)
            if len(a)==N:
                print(a,sum(a))
                
            else:
                if rsearch(N):
                    return True
            del a[-1]
    return False

a = []
rsearch(8)
