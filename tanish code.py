
#code1
a= input("Enter first number: ")
b= input("Enter second number: ")
c= input("Enter third number: ")
avg = (int(a)+int(b)+int(c))/3
print("The average of three numbers is: ", avg) 

#code2
x = float(input("Enter your Gross income: "))
y= int(input("Enter number of dependents: "))
a = (x-10000-(3000*y))
b = a*0.2
print("income Tax is: ", b)

#code3
x  =  [ 21104079, "tanish bansal", "m", "Electrical Engineering", 10]
print(x) 

#code4
x= [21,22,23,24,25]
x.sort()
print(x) 

#code5
x = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
x.pop(3)
print(x)

#code5b 
x = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
del x[3:5]
x.insert(3, "Purple")
print(x)
