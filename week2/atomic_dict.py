print("---- (i) - creating a dictionary ----")
ele={'O':'OXYGEN', 'N':'NITROGEN', 'C':'CARBON'}
print("Original Dictionary :", ele)

print("\n---- (ii) - adding key-value pair to dictionary ----")
sym=input("Enter Unique Symbol : ")
ele[sym]=input("Enter Element : ").upper()
print(ele,"\n")

sym=input("Enter Duplicate Symbol : ")
ele[sym]=input("Enter Element : ").upper()
print(ele)
print('The value for the duplicate key is updated as duplicate keys references to previous data')

print("\n---- (iii) - number of key-value pairs ----")
print("Number of terms in Dictionary :",len(ele))

print("\n---- (iv) - ask user for search element ----")
sym=input("Enter Symbol for element retrieval : ")
if sym in ele:
	print (ele[sym])

elname=input("Enter element for symbol retrieval : ").upper()
if elname in list(ele.values()):
	for i in ele:
		if ele[i]==elname:
			print (i)
