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
		print("encrypted to ",encry(key,clearTextPassword))
	elif (sys.argv[3]=="-de"):
		print("gonna do decryption...")
		encryptedPassword=sys.argv[4]
		print("decrypt to ",decry(key,encryptedPassword))
	else:
		print("wrong syntax. you have to use '-en' or '-de'")
		sys.exit()
	

	#print("key is {}".format(key))

def encry(key,ctpwd):
	if(len(key)!=len(ctpwd)):
		adjustedkey=adjustkey(key,len(ctpwd))
	else:
		adjustedkey=key
	#print("adjusted key is",adjustedkey)
	#encrykey = bin(ctpwd) ^ bin(adjustedkey)
	encrypwd=dothejob(adjustedkey,ctpwd,True)
	return(encrypwd)

def decry(key,enpwd):
	if(len(key)!=len(enpwd)):
		adjustedkey=adjustkey(key,len(enpwd))
	else:
		adjustedkey=key
	#print("adjusted key is",adjustedkey)
	#encrykey = bin(ctpwd) ^ bin(adjustedkey)
	decrypwd=dothejob(adjustedkey,enpwd,False)
	return(decrypwd)
	

def adjustkey(key,leng):
	if (len(key)>leng):
		#reduce key size
		return (key[:leng])
	else:
		#increase key size
		factor=int(leng/len(key))
		#print("factor is",factor)
		tempnewkey=key*(factor+1)
		return tempnewkey[:leng]

def dothejob(key,pwd,en):
	keylist=[]
	pwdlist=[]
	resultlist=[]
	#print("gonna do the job")
	for i in range(0,len(key)):
		if (en==True):
			result=(ord(key[i])^ord(pwd[i]))+33
		else:
			result=(ord(key[i])^(ord(pwd[i])-33))
		resultlist.append(chr(result))
		#print(result)
	#print(resultlist)
	password=""
	for j in resultlist:
		password += j
	return password












if __name__=="__main__":
	main()