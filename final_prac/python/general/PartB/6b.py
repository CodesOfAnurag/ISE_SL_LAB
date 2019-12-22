class Sentences:
    def __init__(self, sent=None):
        self.sent=sent
        self.vowelCount()
    def input(self):
        self.sent=input("Enter Sentance: ")
        self.vowelCount()
    def __reverse(self):
        words=self.sent.split()
        words.reverse()
        self.revSent=" ".join(words)
    def display(self):
        self.__reverse()
        print("Original String:", self.sent)
        print("Reversed String:", self.revSent)
    def vowelCount(self):
        self.count=0
        for i in self.sent:
            if i.lower() in 'aeiou':
                self.count+=1
    def __repr__(self):
        self.__reverse()
        return(self.sent+" --> "+self.revSent)



SentenceList = [Sentences(input(f"Enter Sentence#{i} : ")) for i in range(3)]
ReversedList = sorted(SentenceList , key = lambda x : x.count, reverse=True)
for sentence in ReversedList:
    print(sentence.count,"Vowels :",sentence)