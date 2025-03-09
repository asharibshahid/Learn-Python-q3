#  Maths Play With Numbers    For Developer Play With Python


Age = int(input("Enter your Age  "))

if(Age % 2 == 0):
    print("Its Even Number ")
else:
        print("Its Odd Number")


Num1 = int(input("Enter First number  "))
Num2 = int(input("Enter Secood number  "))
Num3 = int(input("Enter Third number  "))

if(Num1 > Num2 and Num1 > Num3):
    print("Num1 is Greater")
elif(Num2 > Num1 and Num2 > Num3):    
    print("Num2 is Greater")
else:
    print("Num3 is Greater")