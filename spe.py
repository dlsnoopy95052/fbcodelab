#syntax spe.py -k myKey -en myClearTextPassword ==> myEncryptedPassword
#syntax spe.py -k myKey -de myEncryptedPassword ==> myClearTextPassword
import sys

def main():
	clearTextPassword=""
	encryptedPassword=""
	key=""
	print("Starting ...")
	if (len(sys.argv)!=5):
		print("wrong format")
		sys.exit()
	if (sys.argv[1]!="-k"):
		print("wrong syntax. you have to use '-k'")
		sys.exit()
	key=sys.argv[2]
	if (sys.argv[3]=="-en"):
		print("gonna do encryption...")
		clearTextPassword=sys.argv[4]
		print("encrypted to ",encry_decry(key,clearTextPassword,True))
	elif (sys.argv[3]=="-de"):
		print("gonna do decryption...")
		encryptedPassword=sys.argv[4]
		print("decrypt to ",encry_decry(key,encryptedPassword,False))
	else:
		print("wrong syntax. you have to use '-en' or '-de'")
		sys.exit()
	

def encry_decry(key,pwd,en):
	if(len(key)!=len(pwd)):
		adjustedkey=adjustkey(key,len(pwd))
	else:
		adjustedkey=key
	newpwd=dothejob(adjustedkey,pwd,en)
	return newpwd


def adjustkey(key,leng):
	if (len(key)>leng):
		#reduce key size
		return (key[:leng])
	else:
		#increase key size
		factor=int(leng/len(key))
		tempnewkey=key*(factor+1)
		return tempnewkey[:leng]

def dothejob(key,pwd,en):
	keylist=[]
	pwdlist=[]
	resultlist=[]

	for i in range(0,len(key)):
		if (en==True):
			result=(ord(key[i])^ord(pwd[i]))+33
		else:
			result=(ord(key[i])^(ord(pwd[i])-33))
		resultlist.append(chr(result))

	password=""
	for j in resultlist:
		password += j
	return password

if __name__=="__main__":
	main()