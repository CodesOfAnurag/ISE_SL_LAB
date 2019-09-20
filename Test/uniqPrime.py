def prime(x):
    if x>2:
        for i in range(2,x-1):
            if x%i==0:
                return False
        else:
            return True
    elif x==2:
        return True
    else:
        return False

l=[]
while True:
	res = input("Enter Number For List (N-To Stop) : ")
	if res.isdigit():
		l.append(int(res))
	else:
		break
l.sort()
print("Original List : ",l)
lu=list(set(l))
lu.sort()
print("Unique Element List : ",lu)
lp=filter(prime, lu)
print("Prime Number List : ",list(lp))
