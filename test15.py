def hasDup(ints):
	Set=set(ints)

	if (len(ints) == len(Set)):
		print("There is no Dup")
	else:
		print("There is at least one Dup")


ints=[1,2,3,5,4]
hasDup(ints)