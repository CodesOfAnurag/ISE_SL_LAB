from functools import reduce
l = [int(input("Enter Numbers: ")) for i in range(6)]
print("Original List:",l)
ln = list(map(lambda X: X*3, l))
print("Multiplied List:", ln)

print("Sum of Original List Elements:", reduce(lambda x,y: x+y, l))
print("Sum of Multiplied List Elements:", reduce(lambda x,y: x+y, ln))