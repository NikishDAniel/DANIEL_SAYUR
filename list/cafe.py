'''Use lists

1. Write an app for a cafe. Decide on the items in the cafe, stock of each item in the morning, 
stock in the evening, sales amount at the end of the day and profit for each item. You need to restock an item 
if the supply reaches 20% of the stock. Print the 3 items with highest sales, and top 3 highest profit.

'''

'''plan:
    -- list of items , stock in morning , stock in evening
    -- '''

# creating the list for the shop
listOfItems = ['coffee','tea','biscuts','vadai','milk']
itemStock = [80,100,60,110,120]
itemsPrice = [12,15,10,8,14]
itemsSales = [0,0,0,0,0]
itemProfit = [3,4,2,3,2]
itemoredred = [0,0,0,0,0]
customerLimit = 1
customer = 0
menu = ''
quantity = ['1','2','3','4','5','6','7','8','9']
ordered=''
replaceIndex=0

while customer <= customerLimit:
    print(f'Customer {customer+1}:\nmenu:')
    # for loop for display the menu card to every customer
    for item in range(len(listOfItems)):
        itemsMenu=f"{listOfItems[item]} : {itemsPrice[item]} \n"
        if itemsMenu not in menu:
            menu += itemsMenu
    print(menu)
    #closing the for loop to display the menu card
    customerOrdered = input("What do you want?")
    order = customerOrdered.split()
    for i in range(len(order)):
        if order [i] in quantity:
            ordered= order[i]
        if order [i] in listOfItems:
            # index of the ordered item
            index = listOfItems.index(order[i])
            indexOfItems = itemStock[index]
            value = int(indexOfItems) - int(ordered)
            itemStock[index]= value
            itemoredred[index] = int(ordered)
            # items end
            # items price start  
            indexOfPrice = itemsPrice[index]
            newPrice=int(indexOfPrice) * int(ordered)
            assignIndex = itemsSales[index]
            replaceIndex = assignIndex + newPrice
            itemsSales.remove(assignIndex)
            itemsSales.insert(index,replaceIndex)

    customer +=1
# code to display highest sales
Sorted = sorted(itemsSales,reverse=True)
reverse = Sorted[0:3] 
print("Highest sales:")
for item in reverse:
    if item in itemsSales:
        asaw = itemsSales.index(item)
        print(f"the items sold with highest sales : {listOfItems[asaw]} : {item}")
#code for refilling the stock   
for j in range(len(itemStock)):
    if itemStock[j] <= itemStock[j]*0.2:
        print(f"refilling {listOfItems[j]}")
        print(f"{listOfItems[j]} adding =", itemStock[j]-itemStock[j]*0.2)
#code for top 3 highest profit
for i in range(len(itemProfit)):
    itemProfit[i] *= itemoredred[i]
profitReversed = sorted(itemProfit,reverse=True)
profit = profitReversed[0:3]
print("profit: ")
for item in profit:
    if item in itemProfit:
        highProfit= itemProfit.index(item)
        print(f"the items sold with highest profit : {listOfItems[highProfit]} : {item}")