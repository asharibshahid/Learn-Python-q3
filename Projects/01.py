
#  Auto Messaging app Dynamic


Name = input("Enter Your Name ")
date = input("Enter Your Availabilty Date ")
letter  =  "Dear <|Name|> You are selected for the 1st Round of Interview. You are requested to be available on <|Date|>"


print(letter.replace("<|Name|>",Name).replace("<|Date|>",str(date)))