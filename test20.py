def isPrimary(x):
	for i in range(2, x//2+1):
		#print(i)
		if (x%i == 0):
			#print("factor-", i)
			#print("Not primary")
			return False
	return True


#print(isPrimary(16))
i = 168
k=[]
for j in range(2, i//2):
	if (isPrimary(j)):
		if (isPrimary(i-j)):
			print("(",j,i-j,")")
			k.append(j)

print(k[-1], i-k[-1])