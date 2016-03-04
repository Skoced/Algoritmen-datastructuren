'''
Created on 16 feb. 2016

@author: Timo
'''
def swap(a,i,j):
    a[i],a[j]=a[j],a[i]
    
import random
counter = 0
def rqsort(a,low,high):
    global counter
    if low<high:
        counter += 1
        swap(a,low,random.randint(low,high)) #random.randint() is the pivot
        m=low
        for j in range(low+1,high+1):
            if a[j]<a[low]:
                counter += 1
                m += 1
                swap(a,m,j)
                
        swap(a,low,m)
        
        rqsort(a,low,m-1)
        rqsort(a,m+1,high)
        
def qsort(a):
    rqsort(a,0,len(a)-1)
    
def creatlist(a):
    for i in range (0,10000):
        a.append(random.randint(0,256))
        
thelist = []
creatlist(thelist)
qsort(thelist)
print(thelist)
print(counter)