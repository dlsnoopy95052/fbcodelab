def products(nl):
	sort=sorted(nl,reverse=True)
	print(sort[0]*sort[1]*sort[2])

nl=[3,2,9,4,1,7]
products(nl)