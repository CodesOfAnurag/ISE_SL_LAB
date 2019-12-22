# conversion Functions
c2f = lambda c : (c*9/5)+32
c2k = lambda c : (c+273.15)
f2c = lambda f : (f-32)*5/9
f2k = lambda f : (f2c(f)+273.15)
k2c = lambda k : (k-273.15)
k2f = lambda k : (c2f(k-273.15))
# method to select conversion functions based on units passed
method = lambda fromTemp, toTemp ,temp : globals()[fromTemp+"2"+toTemp](temp)
# to hold conversion
conv = list()
# list driven program
while True:
    x=input("Enter\n1 - Convert Temperature\n2 - Show Conversions\n3 - Exit\nResponse: ")
    if x=='1' :
        fromTemp=input("Enter Original Unit (k/c/f): ").lower()
        toTemp=input("Enter New Unit (k/c/f): ").lower()
        if fromTemp in ['k', 'c', 'f'] and toTemp in ['k', 'c', 'f'] and fromTemp!=toTemp :
            temp=float(input("Enter Temperature: "))
            convTemp=round(method(fromTemp, toTemp, temp),2)
            print(temp, fromTemp, "-->", convTemp, toTemp)
            conv.append((str(temp)+fromTemp, str(convTemp)+toTemp))
        else:
            print("Invalid Input")
    elif x=='2' :
        for i in conv:
            print(i[0]+" --> "+i[1])
    elif x=='3' :
        break
    else:
        print("Invalid Input")
