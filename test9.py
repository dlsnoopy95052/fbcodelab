def first(gs):
	counts={}
	for c in gs:
		if c in counts:
			counts[c]+=1
		else:
			counts[c]=1
	print(counts)

	for c in counts:
		if (counts[c]==1):
			print("first non-recurring char is",c)
			break

first("AEEAGHJKZIHJGFRRTKIKL<MKNHTYY&UILKHGTRFT%UJJHHPTFEW")
