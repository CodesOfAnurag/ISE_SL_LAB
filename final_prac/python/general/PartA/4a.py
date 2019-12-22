class Rectangle:
    def __init__(self, l, h):
        self.length = l
        self.height = h
        self.area = 0
    def __Area(self):
        self.area = self.length*self.height
    def printArea(self):
        self.__Area()
        print(self.area)

a=Rectangle(float(input("Enter Length: ")),float(input("Enter Width: ")))
a.printArea()