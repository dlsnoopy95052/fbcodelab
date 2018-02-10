def anagram(s1,s2):
	s1=s1.replace(' ','').lower()
	s2=s2.replace(' ','').lower()

	return sorted(s1)==sorted(s2)

print(anagram("thisa is a dog", "is thi sa dgo"))