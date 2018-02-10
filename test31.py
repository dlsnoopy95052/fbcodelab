def maxsubarray(nlist):
	#splitarray=[[]]*len(nlist)
	splitarray=[[] for _ in range(len(nlist))]
	#print(splitarray)
	index=0
	for i in range(0,len(nlist)):
		#print(i, " ", nlist[i])
		#print("index= ",index)
		if(nlist[i]>=0):
			#print("appending {} to {}".format(nlist[i],index))
			splitarray[index].append(nlist[i])
			#print(splitarray[index], splitarray[index+1])
		else:
			#print("skip {}".format(nlist[i]))
			index += 1
	#print(splitarray[0],splitarray[1])
	answer=calmaxsubarray(splitarray)
	print(splitarray[answer])
def calmaxsubarray(nlist):
	sumofsubarray=[]
	maxsum=0
	maxlen=0
	maxlenpos=0

	for i in range(0, len(nlist)):
		sum=0
		for j in range(0,len(nlist[i])):
			sum += nlist[i][j]
		sumofsubarray.append(sum)
	#print(sumofsubarray)		 
	maxsum=max(sumofsubarray)
	#print(maxsum)
	for i in range(0, len(sumofsubarray)):
		print(i)
		if (sumofsubarray[i]==maxsum):
			currlen=len(nlist[i])
			print("curr len is {}".format(currlen))
			if(currlen>maxlen):
				maxlen=currlen
				maxlenpop=i
	print(maxlenpop)			
	return maxlenpop

A=[-10,1, 2, 5, -7, 2, 3,-1,7,1,1,-2,1,8,2,3]
maxsubarray(A)