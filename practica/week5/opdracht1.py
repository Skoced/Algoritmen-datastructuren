'''
Created on 13 jun. 2016

@author: Timo
'''

INFINITY= float("inf")

class myqueue(list):
    def __init__(self,a=[]):
        list.__init__(self,a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self,x):
        self.append(x)

class Vertex:
    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return str(self.data)
    
    def __lt__(self,other):
        return self.data < other.data
    

def vertices(G):
    a = list(G.keys())
    a.sort()
    return a

def edges(G):
    a = []
    for u in vertices(G):
        for v in G[u]:
            a.append((u,v))
    return a

def BFS(G,s):
    V= vertices(G)
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v !=s:
            v.distance = INFINITY
    q = myqueue()
    q.enqueue(s)
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == INFINITY:
                v.distance = u.distance+1
                v.predecessor = u
                q.enqueue(v)

def show_tree_info(G):
    print('tree:', end = ' ')
    for v in vertices(G):
        print('(' + str(v), end = '') 
        if hasattr(v,'distance'): 
            print(',d:' + str(v.distance), end = '') 
        if hasattr(v,'predecessor'): 
            print(',p:' + str(v.predecessor),  end = '')
        print(')', end = ' ')
    print()
    
def show_sorted_tree_info(G):
    print('sorted tree:')
    V = vertices(G)
    V = [v for v in V if hasattr(v,'distance') and hasattr(v,'predecessor')]
    V.sort(key = lambda x: (x.distance,x.predecessor))
    d = 0
    for v in V:
        if v.distance > d:
            print()
            d += 1        
        print('(' + str(v) + ',d:' + str(v.distance) + ',p:' 
                                                + str(v.predecessor),  end = '')
        print(')', end = ' ')
    print()
    
def is_connected(G):
    V=vertices(G)
    BFS(G,V[0])
    for v in V:

        if hasattr(v,'distance'):
            if v.distance == INFINITY:
                return False
    return True

def nodes_connected(G,s,x):    
    V = vertices(G)
    s.predecessor = None # s krijgt het attribuut 'predecessor'
    s.distance = 0 # s krijgt het attribuut 'distance'
    for v in V:
        if v != s:
            v.distance = INFINITY # v krijgt het attribuut 'distance'
    q = myqueue()
    q.enqueue(s) # plaats de startnode in de queue
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == INFINITY: # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u # v krijgt het attribuut 'predecessor'
                q.enqueue(v) # plaats de buren van v in de queue
                if v == x:
                    return True
    return False

def no_cycles(G):
    V = vertices(G)
    s=V[0]
    s.predecessor=None
    s.distance = 0
    for v in V:
        if v !=s:
            v.distance=INFINITY
    q=myqueue()
    q.enqueue(s)
    while q:
        u=q.dequeue()
        for v in G[u]:
            if v.distance == INFINITY:
                v.distance= u.distance+1
                v.predecessor = u
                q.enqueue(v)
            else:
                if v!=u.predecessor and v.predecessor != None:
                    return False    
    return True

def get_bridges(G):
    edgesListed=edges(G)
    Bridges= list()
    for(first,second) in edgesListed:
        temp = dict(G)
        valuesList = list(temp.get(first))
        valuesList.remove(second)
        temp.update({first:valuesList})
        if nodes_connected(temp,first,second) == False:
            Bridges.append((first,second))
    return Bridges

def is_strongly_connected(G):
    if is_connected(G) == False:
        return False
    
    return True

def remove_edge(G,r,p):
    valueslist= list(G.get(r))
    valueslist.remove(p)
    G.update({r:valueslist})
    valueslist=list(G.get(p))
    if r in valueslist:
        valueslist.remove(r)
        G.update({p:valueslist})
    return G

def is_euler_graph(G):
    V = vertices(G)
    s=V[0]
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v !=s:
            v.distance = INFINITY
    q = myqueue()
    q.enqueue(s)
    while q:
        u = q.dequeue()
        count = 0
        for v in G[u]:
            count = count+1
            if v.distance == INFINITY:
                v.distance = u.distance+1
                v.predecessor = u
                q.enqueue(v)
        if count%2 !=0:
            return False
    return True

def get_euler_circuit(G,start):
    if not is_euler_graph(G):
        return 0
    path = list()
    path.append(start)
    sp = v[start]
    temp=dict(G)
    while True:
        bridges=get_bridges(temp)
        succes = False
        next = None
        for p in temp.get(sp):
            if (sp,p) not in bridges:
                next = p
                succes = True
                break
        if succes == False:
            next = temp.get(sp)[0]
        temp = remove_edge(temp,sp,next)
        sp = next
        path.append(next)
        if next == v[start]:
            break
    return path

v=[Vertex(i) for i in range(8)]

G= {v[0]:[v[1],v[5]],
    v[1]:[v[4],v[5],v[6]],
    v[2]:[v[4],v[5]],
    v[3]:[v[7]],
    v[4]:[v[0],v[1],v[2],v[5]],
    v[5]:[v[0],v[1],v[2],v[4]],
    v[6]:[v[1],v[2]],
    v[7]:[v[3]]} #niet samenhangende graaf voor opdracht 1

G2= {v[0]:[v[1],v[5]],
    v[1]:[v[4],v[5],v[6]],
    v[2]:[v[4],v[5]],
    v[4]:[v[0],v[1],v[2],v[5]],
    v[5]:[v[0],v[1],v[2],v[4]],
    v[6]:[v[1],v[2]]} #samenhangende graaf voor opdracht 1

G3= {v[0]:[v[4],v[5]],
     v[1]:[v[4],v[6]],
     v[2]:[v[5],v[6]],
     v[3]:[v[7]],
     v[4]:[v[0],v[1]],
     v[5]:[v[0],v[2]],
     v[6]:[v[1],v[2]],
     v[7]:[v[3]]} #niet gerichte graaf voor opdracht 2 met cycles

G4= {v[0]:[v[4],v[5]],
     v[1]:[v[4],v[6]],
     v[2]:[v[5]],
     v[3]:[v[7]],
     v[4]:[v[0],v[1]],
     v[5]:[v[0],v[2]],
     v[6]:[v[1]],
     v[7]:[v[3]]} #niet gerichte graaf voor opdracht 2 zonder cycles

G5={v[0]:[v[1],v[3]],
    v[1]:[v[0],v[2]],
    v[2]:[v[1],v[3]],
    v[3]:[v[0],v[2]],
    v[4]:[v[2],v[5],v[6]],
    v[5]:[v[4],v[6]],
    v[6]:[v[4],v[5],v[7]],
    v[7]:[v[6]]} #graaf voor opdracht 3

G6={v[0]:[v[1]],
    v[1]:[v[2]],
    v[2]:[v[0]]} # strongly connected graaf opdracht 4

G7={v[0]:[v[1]],
    v[1]:[],
    v[2]:[v[0],v[1]]} # niet strongly connected graaf opdracht 4

G8={v[0]:[v[1],v[2]],
    v[1]:[v[0],v[3]],
    v[2]:[v[0],v[3]],
    v[3]:[v[1],v[2],v[4],v[6]],
    v[4]:[v[3],v[5],v[6],v[7]],
    v[5]:[v[4],v[6]],
    v[6]:[v[3],v[4],v[5],v[7]],
    v[7]:[v[4],v[6]]}

print(is_connected(G)) #opdracht 1 is een graaf samenhangend
print(is_connected(G2)) # opdracht 1 is een graaf samenhangend
print(no_cycles(G3)) # opdracht 2 met cycles
print(no_cycles(G4)) # opdracht 2 zonder cycles
print("The bridges in G5: ",get_bridges(G5))#opdracht 3 op zoek naar bruggen


print(is_strongly_connected(G6)) #opdracht 4 strong connected
show_tree_info(G6)
print(is_strongly_connected(G7)) #opdracht 5, niet strong connected
show_tree_info(G7)
print(is_euler_graph(G8))
print(is_euler_graph(G7))
print(get_euler_circuit(G8, 0))
