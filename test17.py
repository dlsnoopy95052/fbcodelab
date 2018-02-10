def test(nlist):
	B=dict()
	for i in range(len(nlist)):
		if nlist[i] in B:
			B[nlist[i]] += 1
		else:
			B[nlist[i]] = 1
	for j in B:
		if(B[j] == 1):
			print(j)
A=[1,2,2,3,1]
test(A)

