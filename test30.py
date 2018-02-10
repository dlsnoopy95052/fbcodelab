def wave(nlist):
	nlist.sort()
	print(nlist)
	for i in range(0,len(nlist),2):
		if(i==len(nlist)-1):
			break
		temp=nlist[i]
		nlist[i]=nlist[i+1]
		nlist[i+1]=temp

	print(nlist)

A=[1,3,2,4,5,8,10,6]
wave(A)