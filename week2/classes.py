class person:
	x=0
	def __init__(self,name,age):
		self.name = name
		self.age = age
		person.x+=1
p1=person("Anurag", 20)
p2=person("Anupam", 26)

print ("Name of person #1 is :", p1.name)
print ("Age of person #1 is :", p1.age)
print ("Name of person #2 is :", p2.name)
print ("Age of person #2 is :", p2.age)

p2.age=10
print("Modified age of person #2 is :",p2.age)

print("no of persons :",person.x)
