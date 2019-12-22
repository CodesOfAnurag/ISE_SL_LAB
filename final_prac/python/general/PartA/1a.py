l=list(map(int, input("Enter numbers for the list: ").split()))

while True:
    x = input('''
    Press 1 - Find min and max element
    Press 2 - Insert
    Press 3 - Delete
    Press 4 - Search
    Press 5 - Exit
    Enter Response: ''')
    if x=='1':
        if len(l):
            print(f"Min: {min(l)}\nMax: {max(l)}")
        else:
            print("Empty List")
    elif x=='2' :
        l.append(int(input("Enter Number: ")))
    elif x=='3' :
        if len(l):
            print("Deleted: "+str(l.pop(-1)))
        else:
            print("Empty List")
    elif x=='4' :
        srch=int(input("Enter Element to search: "))
        if srch in l:
            print(f"{srch} is present")
        else:
            print(f"{srch} is not present")
    elif x=='5' :
        break
    else:
        print('Invalid Input')
