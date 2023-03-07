'''3.Write an app to calculate the total bill at the Snack bar. The price of coffee is Rs 100, Vadai (1) is Rs100,
   Sandwich is Rs 200, Coke Rs 60. If the customer buys more than one sandwich or two or more vadai, 
   the price of one coffee  is Rs 50. 
   If the customer buys one of each item, then there is discount of 20% of the total. No further discounts after the 20% discount.
   If the total price of the bill (before any discount) is more than Rs1000, then also there is a 20% discount. '''

#assigning values to the variables 
coffee = 100
vadai = 100
sandwich = 200
coke = 60
total_amount = 0
#getting the number of items as input 
no_of_coffee = int(input("Enter the number of coffee you bought :"))
no_of_vadai = int(input("Enter the number of vadai you bought :"))
no_of_sandwich = int(input("Enter the number of sandwich you bought :"))
no_of_coke = int(input("Enter the number of coke you bought :"))
coffee_1 = 50       # assigning the coffee as 50 to use that in later

# we are checking if the coffee is greater than one or more
if no_of_coffee >= 1:
    print(f"Total coffee you bought {no_of_coffee}.")
    if ( no_of_sandwich > 1 or no_of_vadai > 2 ):
        coffee=coffee_1
        print(f"You bought {no_of_coffee} coffee and {no_of_sandwich} sandwich and {no_of_vadai}vadai .so you got a coffee amount as 50.")
    total_amount = (no_of_coffee*coffee_1) + (no_of_sandwich*sandwich) + (no_of_vadai*vadai) + (no_of_coke*coke)
#suppose we don't buy the coffee we don't need to add them
elif no_of_coffee == 0:
    total_amount = (no_of_coffee*coffee) + (no_of_sandwich*sandwich) + (no_of_vadai*vadai) + (no_of_coke*coke)
#suppose we buy all the items , there is 20 percent discount and if the total bill amount is greater than 1000 then get 20 percent discount
if (no_of_coffee >= 1 and no_of_sandwich >= 1 and no_of_coke >= 1 and no_of_vadai >= 1) or total_amount >=1000 :
    print(f"You bought {no_of_coffee} coffee and {no_of_sandwich} sandwich and {no_of_vadai} vadai and {no_of_coke} coke")
    total_amount = (no_of_coffee*coffee) + (no_of_sandwich*sandwich) + (no_of_vadai*vadai) + (no_of_coke*coke)
    total_amount -= total_amount*0.2

#printing the total salary
print(f"Your total bill amount is {total_amount}")
