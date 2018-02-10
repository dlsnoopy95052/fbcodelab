import math

def isPower(N):
	sqrt = math.floor(math.sqrt(N))
	for p in range(2,33):
		for A in range(2, sqrt+1 ):
			if A**p == N:
				print(A,"**",p)
				return True
	return False
print(isPower(625))