from collections import Counter
from sys import argv
from functools import reduce
try:
    with open(argv[1], 'r') as file:
        words = dict(Counter(sorted(file.read().split())))
except FileNotFoundError as e:
    print(e)

occurence = sorted(words.items(), key=lambda x: x[1],reverse=True)[:10]
print('Occurance:', *occurence)
wordLength = [(i[0],len(i[0])) for i in occurence]
print('WordLength:', *wordLength)
lengths=[i[1] for i in wordLength]
print('AvgLength:', (reduce(lambda x,y: x+y, lengths)/len(lengths)))
print('Sum of Squares of odd lengths:', reduce(lambda x,y : x**2+y**2, [i for i in lengths if i%2==1]))
print('Squares of odd lengths:', *[i**2 for i in lengths if i%2])