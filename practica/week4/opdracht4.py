'''
Created on 20 mrt. 2016

@author: Timo
'''

def F(n):
    #m=[1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]
    m=[10000,5000,2000,1000,500,200,100,50,20,10,5,2,1] #available coins and bills.
    k=[0,0,0,0,0,0,0,0,0,0,0,0,0] #list to show how much bills of what sort are used.
    a=0 #amount of used coins and bills
    if n > 100000:
        print("input is higher than 100000 euro cents, please reduce the input below 100000")
        return 0
    if n<=0:
        print("negative numbers and 0 aren't viable")
        return 0
    usedvalues=[]
    while n > 0:        
        for i in range(len(m)):
            while n-m[i]>=0:
                n= n-m[i]
                a= a+1
                k[i]+=1
                usedvalues.append(m[i])
            print(m[i]," = ", k[i])                                
    print(n,a)
    print(usedvalues,sum(usedvalues))
    return 0

def P(n):
    m=[1,2,5,10,20,50,100,200,500,1000,2000,5000,10000] #available coins and bills.
    k=0 #aantal mogelijkheden
    invert = -1
    n=n+1
    while invert*-1 < len(m):
        if n >= m[invert]:
            break
        del m[-1]
    A = [[0 for y in range (n)]for x in range(len(m))]
    for i in range(len(m)):
        for j in range(n):
            if j >= m[i]:
                A[i][j] = A[i-1][j]+A[i][j-m[i]]
            if j <m[i]:
                A[i][j]=A[i-1][j]
            if j == 0 or i == 0:
                A[i][j]=1
    

    print (A[len(m)-1][n-1])
    return 0    
    
F(3002)    
P(3002)    


        
    