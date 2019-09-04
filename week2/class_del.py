class person:
	x=0
	def __init__(self,name,age):
		self.name = name
		self.age = age
		person.x+=1
	def __del__(self):
		print(self.name,"is dead, we are sorry for your loss")
p1=person("Anurag", 20)
print ("Name of person is :", p1.name)
print ("Age of person is :{}".format(p1.age))

print("deleting object attributes".upper())
del p1.age
print ("Name of person is :", p1.name)
#print ("Age of person is :", p1.age)

print("deleting object itself".upper())
del p1
#print ("Name of person is :", p1.name)
#print ("Age of person is :", p1.age)
