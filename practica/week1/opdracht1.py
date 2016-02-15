'''
Created on 1 feb. 2016

@author: Timo
'''
a = [6,33,5,1,3422,'joost','joop',2,11,33,125,444,12,23410]

def myMax(a):
    k=len(a)
    c=a[0]
    i=0
    while i<k:        
        if isinstance(a[i],int) and c<a[i]:
            c=a[i]
           
        i= i+1
    return c;
print(myMax(a))
