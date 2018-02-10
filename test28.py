def findGCD(m,n):
	smaller=min(m,n)
	larger=max(m,n)
	factors=[]
	
	for i in range(1,smaller+1):
		if(smaller%i==0):
			factors.append(i)
	#print(factors)
	factors = sorted(factors,reverse=True)
	
	#print(factors)
	for j in factors:
		if (larger%j==0):
			return j



print(findGCD(656,388))


