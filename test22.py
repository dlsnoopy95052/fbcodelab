def move(nlist):
	dist=0
	for i in range(len(nlist)-1):
		dist += max(abs(nlist[i][0]-nlist[i+1][0]),abs(nlist[i][1]-nlist[i+1][1]))
	print(dist)

N=[(0,0), (1,0), (3,2), (4,5),(4,-1),(0,0),(-3,-5)]
move(N)