import random
B=[0]*10
for i in range(100000):
	#print(random.uniform(1,100))
	num=random.randint(1,10)
	#print(num)
	B[num-1]+=1
print(max(B),min(B))
