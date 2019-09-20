def divCheck(x):
	if x%5==0 or x%7==0:
		return True
	else:
		return False

l1=[12,24,35,70,88,120,155]

l2=list(set([i if i%2!=0 else None for i in l1]))
_x=l2.pop(0)
l3=[l1[i] for i in range(1,len(l1),2)]

print("Odd Elements : ", l2)
print("Odd Indexed Elements : ",l3)

l2_div=list(filter(divCheck, l2))
l3_div=list(filter(divCheck, l3))
print("Odd Elements Divisible by 5 or 7 : ", l2_div)
print("Odd Indexed Elements Divisible by 5 or 7 : ",l3_div)

