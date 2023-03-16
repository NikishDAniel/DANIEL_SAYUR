listOfItems = ['coffee','tea','biscuts','vadai','milk']
itemStock = [80,100,60,110,120]
itemsPrice = [12,15,10,8,14]
itemsSales = [0,0,0,0,0]
itemProfit = [3,4,2,3,2]
quantity = ['1','2','3','4','5','6','7','8','9']
print(list(enumerate(listOfItems)))
print(list(enumerate(itemStock)))
print(list(enumerate(itemProfit)))
print(list(enumerate(itemsPrice)))
customerLimit = 1
customer = 0
menu = ''
while customer <= customerLimit:
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
        if order [i] in quantity:
            ordered= order[i]
        if order [i] in listOfItems:
            pass
            