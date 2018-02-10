def get_products_of_all_ints_except_at_index(al):
	rl = []
	
	for i in range(0, len(al)):
		value=1
		for j in range(0, len(al)):
			#print (i,j)
			if (j == i):
				continue
			value = value * al[j]
		print(i,j, value)
		rl.append(value)
	return rl

orig=[1, 7, 3, 4]
result=get_products_of_all_ints_except_at_index(orig)
print(result)