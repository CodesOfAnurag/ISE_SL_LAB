students = {1:"Rekha", 2:"Jaya", 3:"Sushma"}
list1 = ["v1", "v2", "v3"]
list2 = list()
j=0
print("-"*50)
for i in students:
	print ("Key :", i,"\nValue :", students[i])
	list1[j]=i
	list2.append(students[i])
	j+=1
print("-"*50)
print("Keys using array :" ,list1)
print("Values using array :" ,list2)
print("-"*50)
print("Keys using methods :" ,list(students.keys()))
print("Values using methods :" ,list(students.values()))
print("Key-Value pairs :",list(students.items()))
print("-"*50)