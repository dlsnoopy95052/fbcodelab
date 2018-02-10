def isPowerof2(A):
	value=A
	#print(value)
	for i in range(64):
		remainder=value%2
		#print(remainder)
		if (remainder != 0):
			return False
		value = value/2
		if (value <= 1):
			break
	return True


print(isPowerof2(128))
