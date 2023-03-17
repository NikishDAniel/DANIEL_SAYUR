'''Use lists
1. Write an app for a cafe. Decide on the items in the cafe, stock of each item in the morning, 
stock in the evening, sales amount at the end of the day and profit for each item. You need to restock an item 
if the supply reaches 20% of the stock. Print the 3 items with highest sales, and top 3 highest profit.
'''
items = {
    "coffee" : {"cost":12,"stock":45,"profit":3},
    "tea" : {"cost":15,"stock":35,"profit":4},
    "vadai" : {"cost":6,"stock":60,"profit":3},
    "biscuts" : {"cost":10,"stock":50,"profit":4},
    "milk" : {"cost":12,"stock":25,"profit":3}
}
menu = ''
quantity = ['1','2','3','4','5','6','7','8','9']
customer = 0
custLimit = 10
while customer<=custLimit:
    print(f'Customer {customer+1}:\nmenu card :')
    # for loop for display the menu card to every customer
    for item in range(len(listOfItems)):
        itemsMenu=f"{listOfItems[item]} : {itemsPrice[item]} \n"
        if itemsMenu not in menu:
            menu += itemsMenu
    print(menu)

    customerOrdered = input("What do you want?")
    order = customerOrdered.split()

    for i in range(len(order)):
        if order[i] in quantity:
            ordered= order[i]