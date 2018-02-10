def findmaxsubarray(nlist):
	oldmaxvalue=0
	newmaxvalue=0
	maxsubarray=[]

	for i in range(len(nlist)):
		if (i==0):
			newmaxvalue=nlist[0]
			oldmaxvalue=newmaxvalue
		print("it is [",nlist[i],"]")
		for j in range(i,len(nlist)):
			#maxvalue=max(maxvalue)
			nextarray=nlist[i:j+1]
			newmaxvalue=max(newmaxvalue,arrayvalue(nextarray))
			if (newmaxvalue != oldmaxvalue):
				maxsubarray=nextarray[:]
				oldmaxvalue=newmaxvalue

		print("***")
	print(newmaxvalue)
	print(maxsubarray)

def arrayvalue(alist):
	total=0
	for i in range(len(alist)):
		total += alist[i]
	return total

A=[1,-3,2,1,-1,3,-4,-1,1,2,-3,3]
findmaxsubarray(A)
#print(arrayvalue(A))