'''
Created on 20 jun. 2016

@author: Timo
'''
import math
import random
class ChainhingHashDemo:
    def __init__(self):
        self.len = 7
        self.table =[None]*self.len
        for itera,dummy in enumerate(self.table):
            self.table[itera] = set()
            itera += 1
    
    def search(self,e):
        for subset in self.table:
            for p in subset:
                if(e == p):
                    return True
        return False

    def countFillingDegree(self):
        cfd = 0
        for itera , value in enumerate(self.table):
            cfd += len(set(value))
            if (cfd / self.len) > 0.75:
                return False
        return True
    
    def insert(self,e):
        temp = hash(e) % self.len
        if not self.search(e):
            if not self.countFillingDegree():
                self.rehash(self.len*2)
            valuesInSet = set(self.table[temp])
            valuesInSet.add(e)
            self.table[temp]=valuesInSet
            return True
        else:
            return False
        
            
    
    def delete(self,e):
        if self.search(e):
            for itera,theSet in enumerate(self.table):
                if set(theSet).__contains__(e):
                    currentSet=set(theSet)
                    currentSet.remove(e)
                    self.table[itera]=currentSet
                    
                    print (e," is gevonden en verwijderd")
                    return True
                itera += 1
        else:
            return False
        
    def __repr__(self):
        output_string="\n---Hash Table ---\n"
        for itera,value in enumerate(self.table):
            output_string += "["+str(itera)+" = " +str(value) +"]\n"
            itera +=1
        output_string += "\nlen = " + str(self.len)
        return output_string
            
    def rehash(self,newLen):
        temp = [None]*newLen
        for itera,dummy in enumerate(temp):
            temp[itera]=set()
            itera+=1
        for subset in self.table:
            for p in subset:
                hashTemp = hash(p) % newLen
                valuesInSet = set(temp[hashTemp])
                valuesInSet.add(p)
                temp[hashTemp] = valuesInSet
        self.table = temp
        self.len = newLen
                
        
demo = ChainhingHashDemo()
RV=[random.uniform(1.3,600) for _ in range (200)]

for i in RV:
    demo.insert(i)

print(demo)
        
for i in RV[100:]:
    demo.delete(i)
    
print(demo)
    