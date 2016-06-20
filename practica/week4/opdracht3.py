'''
Created on 19 mrt. 2016

@author: Timo
'''
def fac(n):
    #print(repr(n)+"!")
    k=0
    p=1
    d=[]
    for i in range(n):
        k=n-i
        p=p*k
        d.append(p)
    #print(d)
    
    return p

def PascallsTriangle(u,d):
    r=[] #up number
    p=[] #prev row
  
    counter=0
    for i in range(u+1):
        c=[] #down number
        p.append(0)
        for k in range(counter+1):
            if k is 0:
                c.append(1)
            else:
                c.append(p[k]+p[k-1])
        p=list(c)
        if counter < d:
            counter+=1
        r.append(c)
    
    printlistVertical(r)
    print(c[d])

    return 0

def printlistVertical(o):
    for i in range(len(o)) :
        print("rij:"+repr(i)+repr(o[i]))

def B(n,k):
    
    return ((fac(n)/fac(k))/fac(n-k))
print(B(7,5))
PascallsTriangle(7,5)
