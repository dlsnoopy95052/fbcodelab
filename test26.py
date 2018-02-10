A=["1","2","it","is","a","book"]

B=""
for i in range(len(A)):
	B += str(A[i]+("!" if (i==len(A)-1) else " "))
print(B)

