#syntax: password-chk.py -ulsn -len 8 -check "T1qV09U"  check if password meets upper, lower, special character, numeric and min length 8
#special character: !@#$ (1-4)

import sys
import re

def password_chk():
	
	if (len(sys.argv)!=6):
		print("wrong syntax")
		return
	pwd = sys.argv[5]
	optallowed=['u','l','s','n']
	options=[]
	minpwdlen = int(sys.argv[3])
	#spc=['!','@','#','$']
	print(minpwdlen)
	for o in sys.argv[1]:
		options.append(o)
	#print(options)
	options=list(set(options) & set(optallowed))
	#print(options)
	print("password check report: {}".format(pwd))
	if (len(pwd) >= minpwdlen):
		print("Length: ok")
	else:
		print("Length: bad")

	for p in range(0,len(pwd)):
		pc = pwd[p]
		#print(pc)
		#if ((pc in "!@#$a-zA-Z0-9")):
			#print("Error: you are using special char not supported")
			#break
		if (options.count('u')>0):
			if (pc.isupper()==True):
				print("Uppercase(u): ok")
				options.remove('u')
		if (options.count('l')>0):
			if (pc.islower()==True):
				print("Lowercase(l): ok")
				options.remove('l')
		if (options.count('n')>0):
			if (pc.isnumeric()==True):
				print("Numeric(n): ok")
				options.remove('n')
		if (options.count('s')>0):
			if (re.match(r"[!@#$]",pc)):
				print("Special char(s): ok")
				options.remove('s')
	for t in range(0,len(options)):
		print(options[t], ": bad")


if __name__=="__main__":
	password_chk()