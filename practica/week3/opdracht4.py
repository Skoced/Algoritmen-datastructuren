from collections import Counter
from operator import itemgetter


def readFile(fileName):
    f = open( fileName, 'r' )  # open een file om uit te lezen
    full_text = ""
    for line in f:
        full_text += line

    for i in full_text:  # clears numbers
        if not i.isalpha( ):
            full_text = full_text.replace( i, ' ' )
    return full_text


def convertTextToList(the_text):
    return [x for x in the_text.split( ' ' ) if x]


def findWordFrequencyMethod1(full_text):
    full_text = Counter( full_text )
    return sorted( full_text.items( ), key=itemgetter( 0 ) )


def findWordFrequencyMethod2(full_text):
    return putInTrie( full_text ).getListTrie()


class trieNode:
    def __init__(self):
        self.count = 0
        self.next = {}

    def addNext(self, key):
        if self.next == {}:
            self.next = {key: trieNode()}
        else:
            if key not in self.next:
                self.next[key] = trieNode()
        return self.next[key]

    def getListTrie(self,retList=[],woord=''):
        if self.count >0:
            retList.append({woord:self.count})
        for henk in sorted(self.next):
            self.next.get(henk).getListTrie(retList,woord+henk)
        return retList

def putInTrie(fullText):
    root = trieNode( )
    i = root
    for char in fullText:
        if char == ' ':
            i.count += 1
            i = root
        else:
            i=i.addNext(char)
    root.count =0#set root count to zero (root cant be a woord)
    return root



print( "Method one is: ", findWordFrequencyMethod1( convertTextToList( readFile( "lorem.txt" ) ) ) )
print("Method two is: ",findWordFrequencyMethod2(readFile( "lorem.txt" )))