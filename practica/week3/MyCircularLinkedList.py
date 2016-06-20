'''
Created on 16 mrt. 2016

@author: Timo
'''
class ListNode:
    def __init__(self,data,next):
        self.data=data
        self.next=next

    
    def __repr__(self):
        return str(self.data)

class MyCircularLinkedList:
    def __init__(self):
        self.tail= None
        
    
    def __repr__(self):
        s=''
        current = None
        if self.tail:
            current=self.tail.next        
            if current != None:
                s=s+str(current)
                current=current.next
            while current!=self.tail.next:
                s=s+"->"+str(current)
                current=current.next
        if not s: #s=='':
            s='empty list'
        return s
    
    def append(self,e):
        current=self.tail
        if not self.tail:
            n=ListNode(e,None)
            self.tail=n
            self.tail.next=self.tail
        else:
            n=ListNode(e,None)
            dummy=self.tail.next
            self.tail=n
            current.next=self.tail
            self.tail.next=dummy
            
           
    
    def delete(self,e):
        if self.tail:
            if self.tail.next.data==e:
                dummy=self.tail.next
                self.tail.next=self.tail.next.next
                if dummy is self.tail.next.next:
                    self.tail=None
                          
            else:
                current=self.tail.next.next
                dummy=self.tail.next
                while current.next.data is not e and current is not dummy:
                    current=current.next
                if current.next.data is e:
                    current.next=current.next.next


mylist=MyCircularLinkedList()
print(mylist)
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist)
mylist.delete(2)
mylist.append(5)
print(mylist)
mylist.append(5)
print(mylist)
mylist.delete(5)
print(mylist)
