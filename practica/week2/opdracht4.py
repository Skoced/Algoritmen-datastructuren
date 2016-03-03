def mybin(n):
	try:
		n = int(n)
		assert n >= 0
		if n == 0:
			return '0b'
		return mybin(n//2) + str(n % 2)
	except ValueError:
		return "NaN"
	except AssertionError:
		return "value less than zero"

print(mybin("Bla"))
print(mybin("0.1"))
print(mybin("100"))