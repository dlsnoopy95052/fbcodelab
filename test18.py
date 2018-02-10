def singleNumber(A):
    ret = A[0]
    print(ret)
    for i in range(1,len(A)):
        ret ^= A[i]
        print("..",ret)
    print(ret)
    return ret

B=(1,2,2,3,1,4,3,5,5)
singleNumber(B)