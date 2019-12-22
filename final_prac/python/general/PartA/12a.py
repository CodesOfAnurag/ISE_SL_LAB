class Student:
    def __init__(self, name=None, age=None, p=None, c=None, m=None):
        self.name=name
        self.age=age
        self.mark=[p,c,m]
    def accept(self):
        self.name=input("Name: ")
        self.age=input("Age: ")
        self.mark=[int(input("Physics Marks: ")), int(input("Chemistry Marks: ")), int(input("Mathematics Marks: "))]
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Physics Marks:",self.mark[0])
        print("Chemistry Marks:",self.mark[1])
        print("Mathematics Marks:",self.mark[2])

std1=Student()
std2=Student()
print("*"*25,"\nEnter Data")
std1.accept()
print("-"*25)
std1.display()
print("*"*25,"\nEnter Data")
std2.accept()
print("-"*25)
std2.display()
print("*"*25)