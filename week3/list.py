def remDupli1(l):
	return list(set(l))

def remDupli2(l):
	l2=list()
	for i in range(len(l)):
		if l[i] not in l[i+1:]:
			l2.append(l[i])
	return l2

def rev(l):
	return l[::-1]


l1=list()

while True:
	x=input("Enter Number(N-to stop) : ")
	if x=='N' or x=='n':
		break
	else:
		l1.append(int(x))



print("List without duplicate elements (method1) : ",remDupli1(l1))
print("List without duplicate elements (method2) : ",remDupli2(l1))

print("Orignal list : ",l1)
print("Reversed list : ", rev(l1))

print("List of Even numbers till 20 : ", [ i for i in range(0,21,2)])
