'''
Created on 8 feb. 2016

@author: Remco
'''
def getNumbers(s):
    clist = list(s)
    cnew = []
    for x in clist:
        if x < '0' or x > '9':
            cnew.append(' ')
        else:
            cnew.append(x)
    clist = ''.join(cnew)
    cnew = clist.split()
    return cnew

print(getNumbers("een123zin45 6met-632meerdere+7777getallen"))