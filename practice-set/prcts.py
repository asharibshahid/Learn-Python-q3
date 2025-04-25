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
#         print("Sorry You Are Under Age ")



# nAmee = input("enter Your Name ")
# AAgee = input("Enter Your Age ")

# printingMyName(nAmee, int(AAgee))



#  Oops


# class Employee:
   
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def getSalary(self):
#           return self.salary


# asharib = Employee("Asharib", "100000")
# print(asharib.salary)
# print(asharib.name)


# Sets
# Ye Double Value ko ignre krta hai aur Ye Aik Unordered Collection hai
#  Aur iska Data Type Set hai

# set1 = {1,4,6,"asharib" , "hello", "hello"}
# print (set1)
# print(type(set1))

# my_dict = {
#     "cat": "a Small animal",
#     "table": ["A furniture", "A place to study"],
# }

# cls_count =  { "python" ,"python" ,"javascript" , "typescript" , "python" , "java" , "typescript" }
# final = len(cls_count)

# print(f"We Wanna {final} Classrooms") 

# colors ={"red" , "blue" , "green" , "yellow"}
# for i in colors:
#     print(i)
#     if i == "red":
#        print(i+"Humm")
#     elif i == "yellow":
#         print(i+ "  Ye hy yellow")


# for i in range(2,90):
#     print(f"A{i}")


# class person():
#     name ="asharib",
#     age = 16,
#     love = "None",



# a = person()     # Now Just asharib 
# a.name = "Sheikh"  #Now Sheikh Instead Of asharib


# print(a.name)


# class person:
#     name ="asharib",
#     age = 16,
#     love = "None",
#     occ = " Developer"
#     def Info(self):
#         print(f"{self.name} is a {self.occ}")

# b = person()
# b.I()

# def q1(name):
#     print(f"Hello {name} WAelcome")

# q1(input("Enter Your Name "))    
# student = {"name": "Ahmed", "age": 18}

# for value in student.items():
#     print(f" {value}")

# List:int = [5, 10, 15] 
# def avrg(List):
#      avg= sum(List) / len(List)
#      print(f"Average is {avg}")

# avrg(List)     

# nums = [1, 2, 3, 4, 5]
# print(nums[::-1])  # 


# vowels = ['a', 'e', 'i', 'o', 'u']
# def Check_Vowel(vowels):
#     name = input("Enter Your Name ")
#     if name.lower() in vowels:
#         print(f"{name} is a Vowel")
#     else:
#         print(f"{name} is not a Vowel")



# Check_Vowel(vowels)

# my_dict={"name":"asharib" , "age": 23, "address": {"location": "karachi"}  }
# my_set = {1, 2, 3, 4, 5}
# for my_set in range(5):
#     print(my_set)

# a={1,2,3,4,5}
# b={4,5,6,7,8}
# Nums = a.union(b)
# print(Nums)


# my_set = {1, 2, 3, 4, 5}
# my_set2 = {4, 5, 1, 7, 2}
# intersection= my_set.intersection(my_set2)
# print(intersection)


# file_name= input("Enter Your File Name ")
# with open(file_name, "r") as file:
#     for line in file:
#         words=line.split()
#         print(words)
# print("Please Enter Words To Count The Number of Words")
# words = input("Enter a string: ")
# def word_counter(words):
#     word_nospace = words.replace(" ", "")
  
#     word_count = len(word_nospace)
#     print(f"The number of words in the string is: {word_count}")


# word_counter(words)    


# Data = [0,4,3,2,3,5,8,9,10]
# Data.sort()
# def find_Even_odd(Data):
#     even = []
#     odd = []
   
#     for i in Data:
#         if i % 2 == 0:
#            even.append(i)
#         else:
#             odd.append(i)
#     print(f"Even Numbers are {even}")
#     print(f"Odd Numbers are {odd}")




# find_Even_odd(Data)    


# put_name = input("Enter the 1st String ")
# put_name.split(",")
# put_name2 = input("Enter the 1st String ")
# put_name2.split(",")
# set(put_name)
# set(put_name2)
# common = set(put_name).intersection(set(put_name2))
# print(f"Common Elements are {common}")

# inp=input("Enter Your String ")


# def justAlphabets(Inp):
#     if inp.isalpha():
#         print("String is Alphabetic")
#     else:
#         print("String is not Alphabetic")
# justAlphabets(inp)        


# my_dict = {"apple": 3, "banana": 1, "cherry": 2}
# sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
# print(sorted_dict)

# get_num = input("Enter Your Number to perform operation:  ")

# get_num2 = input("Enter Your 2nd Number to perform operation:  ")
# ops:int = input('Please enter The Operation you want to - , + , x , % :  ')
# for op in ops:
#     if op == '-':
#         print(int(get_num) - int(get_num2))
#     elif op == '+':    
#         print(int(get_num) + int(get_num2))
#     elif op == 'x':
#         print(int(get_num) * int(get_num2))
#     elif op == '%':
#         print(int(get_num) / int(get_num2))
#     else:
#         print("Please Enter Valid Operation")
#         break



# students = {
#     "Ali": [85, 90, 78],
#     "Sara": [88, 76, 92],
#     "Zain": [95, 91, 89]
# }
# ali = students["Ali"]
# avrg1 = sum(ali) / len(ali)
# zain = students["Zain"]
# avrg2 = sum(zain) / len(zain)
# sara = students["Sara"]
# avrg3 = sum(sara) / len(sara)

# final_avaerage= print(avrg1,avrg2,avrg3)




# class Private:
#     def _init_(self , name , salary):
#         self.name = name 
#         self.salary = salary
        
  
#         print(f"The name is {name}  and your salary is {salary}")   

# Private("ayesha" , 890)


# class Students:
#     def __init__(self , name , marks):
#         self.name = name
#         self.marks = marks

#     def average(self):
#         plus = sum(self.marks) / len(self.marks)
#         print(f"Average Marks of {self.name} is {plus}")



# s1 = Students("Ali", [85, 90, 78])
# print(s1.marks)
# s1.average()


