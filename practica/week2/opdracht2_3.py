'''
Created on 8 feb. 2016

@author: Timo
'''

class mystack(list):

    def push(self,i):
        self.append(i)
        print("push")
        
    def pop(self):
        if self.isempty()==False:
            k = (len(self))-1
            del(self[k])
        
        
    def peek(self,a):
        if len(self)<=a:
            print(len(self))
            print("out of range")
            return None
        else:
            return(self[a])
        
    def isempty(self):
        if len(self)==0:
            print("is empty")
            return True
        return False
        

d = "(<[{<>}]>)"
g = mystack([22,33,44,11,12,13,14])
print(g.peek(-2))
def parenthesischeck(s):
    a = mystack([])
    clist = list(s)
    b = 'k'
    for x in (clist):
        a.push(x)
        if len(a)>1:
            b = a.peek(-2)            
        if ord(x)-2 == ord(b) or ord(x) -1 == ord(b):
            a.pop()
            a.pop()


    if a.isempty()==False:
        print("Parenthesis don't line up",a)
    else:
        print("Parenthesis are correct")
parenthesischeck(d)