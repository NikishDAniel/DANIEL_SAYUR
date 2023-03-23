'''Use lists
1. Write an app for a cafe. Decide on the items in the cafe, stock of each item in the morning, 
stock in the evening, sales amount at the end of the day and profit for each item. You need to restock an item 
if the supply reaches 20% of the stock. Print the 3 items with highest sales, and top 3 highest profit.
'''

# creating dictionary items and necessary key value pair
items = {
    "coffee" : {
        "cost":12,
        "stock":45,
        "profit":3,
        "price":0,
        "profitNew":0,
        "refill":100
        },
    "tea" : {
        "cost":15,
        "stock":35,
        "profit":4,
        "price":0,
        "profitNew":0,
        "refill":100
        },
    "vadai" : {
        "cost":6,
        "stock":60,
        "profit":3,
        "price":0,
        "profitNew":0,
        "refill":100
        },
    "biscuts" : {
        "cost":10,
        "stock":50,
        "profit":4,
        "price":0,
        "profitNew":0,
        "refill":100
        },
    "milk" : {
        "cost":12,
        "stock":25,
        "profit":3,
        "price":0,
        "profitNew":0,
        "refill":100
        }
}
menu = ''
#creating two empyt list so that we can calculate the top three highest profit and price 
priceList = []
profitList = []
#creating the list for taking the quantity of the items
quantity = ['1','2','3','4','5','6','7','8','9']
#initialize the customer to 0
customer = 0
#setting the customer limit 
customerLimit = 3
for keys in items:
    menu += keys + "\n"
'''def main():
    for i in range(len(order)): 
        if order[i] in quantity:
            ordered = order[i]  

        if order[i].isalpha():
            if order[i] != "and":
                itemOrdered = order[i]
                '''
# to create a loop to check the condition that the customer less or equal to customer limit
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

        if order[i].isalpha():
            if order[i] != "and":
                itemOrdered = order[i]
                stock = items[itemOrdered]['stock']
                if stock < stock*0.2:
                    print(f"Refilling {itemOrdered}")
                cost = items[itemOrdered]['cost']
                
                profit = items[itemOrdered]['profit']
                newProfit = int(profit)*int(ordered)
                enumerated = items[itemOrdered]['profitNew']
                enumerated += newProfit  
                newStock = int(stock)-int(ordered)
                amount = int(ordered)*int(cost)
                newPrices = items[itemOrdered]['price']
                newPrices += amount
                items[itemOrdered]["price"]=newPrices
                items[itemOrdered]["stock"]=newStock
                items[itemOrdered]["profitNew"]=enumerated
    customer += 1
print(items)
for key in items:
    x=items[key]["price"]
    priceList.append(x)
enumerated=list(enumerate(priceList))
rev = sorted(enumerated,key=lambda x:x[1],reverse=True)
highestPrice = rev[0:3]
print(highestPrice)
print("Highest price sold items :")
for i in highestPrice:
    print(f"{list(items)[i[0]]} : {i[1]}")
    
for key in items:
    x=items[key]["profitNew"]
    profitList.append(x)
enumerated=list(enumerate(profitList))
rev = sorted(enumerated,key=lambda x:x[1],reverse=True)
highestProfit = rev[0:3]
print(highestProfit)
print("Highest profit sold items :")
for j in highestProfit:
    print(f'{list(items)[j[0]]}:{j[1]}')