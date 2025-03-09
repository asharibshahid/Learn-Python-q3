# Indexing 



# str="pakistan"
# print(str[2])

# SLICING
# It It also working with backward like -1 -2



# name = "asharibSheikh"
# print(name[1:13])

# Functioon String

# str="pakistam"
# print(str.endswith("n"))


# str = print(str.capitalize())
# print(str2)

# Replacing
# print(str.replace("m","n"))




# name =input("Enter your f-name: ")
# print(name.__len__())


#  if elif else 

# age = 17

# if(age >= 18):
#     print("you are Eligiible To Vote" ) 

# elif(age >= 17):
#         print("Please Wait for One Year")
# elif(age >= 16):
#     print("Please Wait for Two Year")        

# else: print("You are not Eligible to Vote")

#  Challenge 

# Age = int(input("Enter your Age  "))

# if(Age % 2 == 0):
#     print("Its Even Number ")
# else:
#         print("Its Odd Number")


# Num1 = int(input("Enter First number  "))
# Num2 = int(input("Enter Secood number  "))
# Num3 = int(input("Enter Third number  "))

# if(Num1 > Num2 and Num1 > Num3):
#     print("Num1 is Greater")
# elif(Num2 > Num1 and Num2 > Num3):    
#     print("Num2 is Greater")
# else:
#     print("Num3 is Greater")


# Name = input("Enter Your Name ")
# date = input("Enter Your Availabilty Date ")
# letter  =  "Dear <|Name|> You are selected for the 1st Round of Interview. You are requested to be available on <|Date|>"


# print(letter.replace("<|Name|>",Name).replace("<|Date|>",str(date)))


#  List


# marks =[ 4.5 , 6 ,7, 777,8]


# Slicing


# print(marks[2:5])





# Negative Index Slicing and Methods

# marks =[ 4.5 , 6 ,7, 777,8]
# print(marks[-0:-3])



# Its Add An New Element
# marks.append(9)
# Applies  Accending Order
# marks.sort()


# Tuples 
# tup = (1,2,3,4, 5, 6 , 2)
# print(tup[3])
# print(tup[3:5])
# print(tup.index(4))
# print(tup.count(2))

#  Wap Prcts


# print("Enter Your 3 Favourite Movies ")

# movie1= input("First Movie  ")
# movie2= input("Second Movie  ")
# movie3= input("Third Movie  ")
# list = {movie1, movie2, movie3}


# print(list)


# Wap  check  Palindrome
# list = ["asharib", "sheikh", "sheikh", "asharib"]

# list.copy()

# list.reverse()

# print(list)


# Grades = ( "a" , "b ", "c", "d" ,"a" , "a")



# print(Grades.count("a"))


# grades = ["d" , "b" , "c" , "a" ]
# grades.sort()
# print(grades)

# Dictionary 


# dic = {
#     "name" :"asharib",
#     "age" : 23,
#     "class" : "AI",
# "ali" : {
#     "name" :"Ali Ahmed",
#     "age" : 22,
#     "class" : "AI"
# }

# }
# print(dic["name"])
# print(dic["ali"])

#  Dict Methods 

# print(dic.keys())
# print(dic.values())
# print(dic.items())

# dic = { 
#      "Name" :  "asharib",
#      "class" : "9th",
#      "location" : "karachi"

# }


# print(dic.get("Name"))


# Loops 


# a = 5
# match a:
#     case 5:
#         for a in range(5):
#             print(a*2)
#     case 6:
#         print("This is 6")


# a = [21,23,33,222,43]
# b= {21,23,33,222,43}
# for item in a:
#     print(item*b)


# while True:
#     print("Enter Your Name ")
#     name = input()
#     if name.isalpha():
#         print("Thanks")
#         break
#     else:
#         print("Please Enter Your Name")
#         continue


# while (True):
#     num = int(input("Plese Enter First Number:  "))
#     print(num)
#     if(num >10):
#         print("You Enter The Greater number OUt OF 10 The Code Will Break")
#         break


#  Functions 
# def  printingMyName(name , age):
#     print(f"my Name Is {name} and My Age is {age}")
#     if age >= 18:
#         print("You are Eligible to Vote")
#     elif age >= 17:
#             print("Please Wait for One Year")
#     else:
#         print("Sorry")



# nAmee = input("enter Your Name ")
# AAgee = input("Enter Your Age ")

# printingMyName(nAmee, int(AAgee))

#  Oops


class Employee:
   
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def getSalary(self):
          return self.salary


asharib = Employee("Asharib", "100000")
print(asharib.salary)
print(asharib.name)
