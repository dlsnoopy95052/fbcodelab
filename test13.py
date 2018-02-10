def add(lst, num):
	newv=lst[len(lst)-1]+num
	addf=False
	if (newv>=10):
		lst[len(lst)-1] = newv % 10
		for i in range(len(lst)-2, -1, -1):
			if ((lst[i]+1) >= 10):
				lst[i]=0
				if (i==0):
					addf=True
					break
				continue
			else:
				lst[i]+=1
				break
	else:
		lst[len(lst)-1] = newv
	if (addf == True):
		lst.insert(0,1)
	return lst



ol=[9,9,9,9,9,9,9,9,9]
print(ol)
nl=add(ol, 9)
print(nl)