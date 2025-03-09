#  Cafe Management System

menu = {
   'Pizza' : 5.00,
    'Burger' : 3.00,
   'Coke' : 1.00,
    'Fries' : 1.50,
   'Sandwich' : 2.50
}


print("Welcome to the Our Cafe")

print("Pizza Rs 5.00 \nBurger Rs 3.00 \nCoke Rs 1.00 \nFries Rs 1.50 \nSandwich Rs 2.50")

order_Total = 0


item_1 = input("Enter Your First Item ")
if item_1 in menu:
    order_Total += menu[item_1]
    print(f"{item_1} Added to your Cart")
else:
    print(" Sory Item Not Available")

item_2 = input(" You Wanna Order Something More ?? (yes/no) ")

if item_2 == "yes":
   if item_2 in menu:
    order_Total += menu[item_2]
    print(f"{item_2} Added to your Cart")
else:
    print(" Sory Item Not Available")

    print(f"Your Total Bill is {order_Total}")