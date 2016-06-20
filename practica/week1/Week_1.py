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

import random

def randExperiment():
	genTimes = 100
	numTimes = 0
	persons = 23
	for times in range(0, genTimes):
		l = []
		for i in range(0, persons):
			l.append(random.randint(1,365))
		for date in l:
			for x in range(date + 1, len(l)):
				if l[date] == l[x]:
					numTimes += 1
	return numTimes / genTimes * 100


print("2.")
print(getNumbers("een123zin45 6met-632meerdere+7777getallen"))
print("4.")
print(str(randExperiment()) + "%")