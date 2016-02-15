'''
Created on 8 feb. 2016

@author: Remco
'''
import random


def randExperiment():
    genTimes = 10000
    numTimes = 0
    persons = 23
    equal = False
    for dummy in range(0, genTimes):
        k = []
        for _ in range(0, persons):
            k.append(random.randint(1,365))
        for date in range(0,len(k)):
            for x in range(date+1,len(k)):
                if k[date] == k[x] and x != date:
                    #print(k[date],"-",k[x],date,"-",x)
                    equal= True
        if equal:
            numTimes +=1
            equal = False    
    return numTimes / genTimes * 100
print(randExperiment(),"%")