def check(value):
	valueset=set()
	for c in range(0, len(value)):
		if (value[c] in valueset):
			return value[c]
		else:
			valueset.update(value[c])
	return "nothing" 



Value="CDEFAJTYY"

print(check(Value))