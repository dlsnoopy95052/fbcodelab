def square(nums):
	results=[]
	for num in nums:
		yield(num ** 2)
	

mynums = (x**2 for x in [5,4,3,2,8])

print(mynums)

for num in mynums:
	print(num)