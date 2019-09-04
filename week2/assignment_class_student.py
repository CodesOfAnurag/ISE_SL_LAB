class Student:
	def __init__(self,name="Anurag",age=20):
		self.name = name
		self.age = age

	def display(self):
		print("Name :", self.name)
		print("Age :", self.age)

	def entry(self):
		print("Modify Data :")
		self.name=input("Enter new name :")
		self.age=input("Enter new age :")
	
st1=Student()
'''
st1.display()
st1.entry()
st1.display()
'''
while True:
	res=int(input('Enter Response (1-display, 2-modify, 3-quit) :'))
	if res == 1:
		st1.display()
	elif res ==2:
		st1.entry()
	elif res ==3:
		exit(0)
	else:
		print("Invalid Response")
		 

