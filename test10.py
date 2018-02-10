def get_max(spy):
	maxv=0
	for i in range(0, len(spy)):
		for j in range(i+1, len(spy)):
			diff = spy[j]-spy[i]

			if (diff > maxv):
				maxv=diff
				trade = "buy at "+str(spy[i])+" sell at "+str(spy[j])
				print(maxv, trade, i, j)
	#print(maxv, trade)			




spyvalue=[10, 7, 5, 8, 11, 9, 4, 10, 18, 1, 7, 9, 12, 6]
get_max(spyvalue)