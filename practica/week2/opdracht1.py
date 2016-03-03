def machtv3(a,n):
	assert n >= 0
	if n == 0:
		return 1
	if a == 0:
		return 0
	m = 1
	while n > 1:
		if n%2 == 1:
			m = m*a
		n = n//2
		a = a*a
	print("Multiplication times (m): " + str(m))
	return m*a

print(machtv3(2,10000))