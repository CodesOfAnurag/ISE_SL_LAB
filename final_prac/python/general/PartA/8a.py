atom = {'O' : 'Oxygen', 'H' : 'Hydrogen', 'C' : 'Carbon', 'Si' : 'Silicon'}

print("Original Dictionary: ",atom)

while(True):
    x=input("Adding Duplicate Key : ")
    if x in atom:
        atom[x]=input("Enter Element: ")
        print("Changed Dictionary: ",atom)
        break
    else:
        print("Not already present in Dictionary")

while(True):
    x=input("Adding New Key : ")
    if x not in atom:
        atom[x]=input("Enter Element: ")
        print("Changed Dictionary: ",atom)
        break
    else:
        print("Already present in Dictionary")

print("Number of elements in Dictionary:", len(atom))

x=input("Enter Search Symbol: ")
if x in atom:
    print(x,":",atom[x])
else:
    print("Not Present in Atom Dictionary")