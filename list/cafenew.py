''' 2. Extension of Cafe  
2.1Replenish supply for every 5 customers  and at the end of the day
2.2 Calculate replenish supply at the starting of the day for hot items,
every 5 customers for all items and only cold items at the every end of the day.'''

# creating dictionary items and necessary key value pair
items = {
    "coffee" : {
        "cost":12,
        "sto" : 45,
        "stock":45,
        "profit":3,
        "price":0,
        "profitNew":0,
        "hot item":1
        },
    "tea" : {
        "cost":15,
        "sto" : 35,
        "stock":35,
        "profit":4,
        "price":0,
        "profitNew":0,
        "hot item":1
        },
    "vadai" : {
        "cost":6,
        "sto" : 60,
        "stock":60,
        "profit":3,
        "price":0,
        "profitNew":0,
        "hot item":1
        },
    "biscuts" : {
        "cost":10,
        "sto" : 50,
        "stock":50,
        "profit":4,
        "price":0,
        "profitNew":0,
        "hot item ": 0
        },
    "milk" : {
        "cost":12,
        "sto" : 25,
        "stock":25,
        "profit":3,
        "price":0,
        "profitNew":0,
        "hot item":1
        }
}
#initializing the customer and customer limit 
menu = ''
#creating two empyt list so that we can calculate the top three highest profit and price 
"""priceList = []
profitList = []"""
totalPrice = 0
totalRelpenishHot = 0
totalRelpenishCold = 0
#creating the list for taking the quantity of the items
quantity = ['1','2','3','4','5','6','7','8','9']
#initialize the customer to 0
customer = 0
#setting the customer limit 
customerLimit = 5
# defining the function for items replenish
def replenish(items):
    for item in items.keys():
        items[item]["stock"]=items[item]["sto"]
    return items
# defining the function for hot items replenish
def replenishHot(add):
    hotVal = 


def replenishCold():

#checking for 
while customer<=customerLimit:
    print(f'Customer {customer+1}:\nmenu card :')
    print(menu)
    # getting input from customer
    customerOrdered = input("What do you want?")
    order = customerOrdered.split()
    #seperating the quantity and items that are ordered
    for i in range(len(order)): 
        if order[i] in quantity:
            ordered = order[i]  
        # getting the items
        if order[i].isalpha():
            if order[i] != "and":
                itemOrdered = order[i]
                stock = items[itemOrdered]['stock']
                newStock = int(stock)-int(ordered)
                # checking for the stock
                if customer > 5:
                    if items[itemOrdered]["hot items"] == 1:
                        stockNew = int(items[itemOrdered]["sto"])
                        hotStock = int(stockNew - 5)
                        print(f"Refilling {itemOrdered}")
                        print(f"Adding {hotStock } stock of {itemOrdered}")
                        totalRelpenishHot +=hotStock 
                    if items[itemOrdered]["hot items"] == 0:
                        stockNew = int(items[itemOrdered]["sto"])
                        coldStock = int(stockNew - 5)
                        print(f"Refilling {itemOrdered}")
                        print(f"Adding {coldStock} stock of {itemOrdered}")
                        totalRelpenishCold += coldStock
                cost = items[itemOrdered]['cost']
                profit = items[itemOrdered]['profit']
                newProfit = int(profit)*int(ordered)
                enumerated = items[itemOrdered]['profitNew']
                enumerated += newProfit  
                amount = int(ordered)*int(cost)
                newPrices = items[itemOrdered]['price']
                newPrices += amount
                items[itemOrdered]["price"]=newPrices
                items[itemOrdered]["stock"]=newStock
                items[itemOrdered]["profitNew"]=enumerated
    customer += 1
     