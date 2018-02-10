def lightbulb(nlist):
	for i in range(0, len(nlist)):
		if (nlist[i] == 0):
			
			#print(nlist)
			nlist[i] = 1
			for j in range(i+1, len(nlist)):
				nlist[j] ^= 1
			print("click switch", i, nlist)







B=[0,1,0,1,1,0,0,0,1,0]
lightbulb(B)