
def getsubset(nlist):
	

	init=0
	null = "null"


	for i in (null, nlist[0]):
		print(i)
		recursearch(1,nlist)

def recursearch(number,nlist):
	global howmany
	null="null"
	if (number==len(nlist)):
		howmany+=1
		return
	else:
		for i in (null, nlist[number]):

			print("-"*number*5,i)
			recursearch(number+1,nlist)

howmany = 0
nl=[1,2,6,9,5]
getsubset(nl)
print(howmany)