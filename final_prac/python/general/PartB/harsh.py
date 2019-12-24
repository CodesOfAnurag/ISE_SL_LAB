class line:
    def __init__(self, arg=""):
        self.sentence=arg
        self.count=self.vowels()
        self.revLine()
    def vowels(self):
        cnt=0
        for i in self.sentence:
            if i.lower() in 'aeiou':
                cnt+=1
        return cnt
    def revLine(self):
        word=self.sentence.split()
        word.reverse()
        self.rev=" ".join(word)
    def display(self):
    	print(self.sentence, ":", self.rev,":",self.count,"Vowels")
    



a1=line(input("String1: "))
a2=line(input("String2: "))
a3=line(input("String3: "))

lineList=[a1,a2,a3]
sortLineList=sorted(lineList, key=lambda x:x.count ,reverse=True)
for i in sortLineList:
    i.display()
