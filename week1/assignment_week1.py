#list man
#----------------------q2-------------------------
#main list
l1=[1,2,34,12,4313,21]
print ("l1 :",l1)
#new list
l2=list(l1)
print ("new l2 :",l2)
#slice
print ("sliced l2 :",l2[2:])
#replace
l2[1]=1000000
print ("changed l2 :", l2)
#add two list
l3=l1+l2
print ("added list l2:",l3)
#copying
l4=list(l3)
l5=l3[:]
#splitting into chunks
lm=list(range(100))
step=10
l_chunk=[lm[i:i+10] for i in range(0,100,10)]
print ("Chunked list : ")
for i in l_chunk:
	print (i)
#----------------------q2-------------------------
#tuple creattion
t1=tuple(range(10))
print("Tuple :",t1)
print(t1[1])
#----------------------q3-------------------------
#convert list to tuple
t2=tuple(l1)
print ("Converted from list :",t2)

