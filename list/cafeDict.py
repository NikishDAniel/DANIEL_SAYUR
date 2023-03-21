'''Use lists
1. Write an app for a cafe. Decide on the items in the cafe, stock of each item in the morning, 
stock in the evening, sales amount at the end of the day and profit for each item. You need to restock an item 
if the supply reaches 20% of the stock. Print the 3 items with highest sales, and top 3 highest profit.
'''
items = {
    "coffee" : {"cost":12,"stock":45,"profit":3,"price":0,"profitNew":0,"refill":100},
    "tea" : {"cost":15,"stock":35,"profit":4,"price":0,"profitNew":0,"refill":100},
    "vadai" : {"cost":6,"stock":60,"profit":3,"price":0,"profitNew":0,"refill":100},
    "biscuts" : {"cost":10,"stock":50,"profit":4,"price":0,"profitNew":0,"refill":100},
    "milk" : {"cost":12,"stock":25,"profit":3,"price":0,"profitNew":0,"refill":100}
}
menu = ''
priceList = []
profitList = []
quantity = ['1','2','3','4','5','6','7','8','9']
customer = 0
custLimit = 1
while customer<=custLimit:
    print(f'Customer {customer+1}:\nmenu card :')
    for keys in items:
        print(keys)

    customerOrdered = input("What do you want?")
    order = customerOrdered.split()

    for i in range(len(order)):
        if order[i] in quantity:
            ordered= order[i]

        if order[i].isalpha():
            if order[i] != "and":
                itemOrdered = order[i]
                cost = items[itemOrdered]['cost']
                stock = items[itemOrdered]['stock']
                profit = items[itemOrdered]['profit']
                newProfit = int(profit)*int(ordered)
                enumerated = items[itemOrdered]['profitNew']
                enumerated += newProfit  
                newStock = int(stock)-int(ordered)
                amount = int(ordered)*int(cost)
                k = items[itemOrdered]['price']
                k += amount
                items[itemOrdered]["price"]=k
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
print("Highest price sold items :")
for i in highestPrice:
    print(f"{list(items)[i[0]]} : {i[1]}")
    
for key in items:
    x=items[key]["profit"]
    profitList.append(x)
enumerated=list(enumerate(profitList))
rev = sorted(enumerated,key=lambda x:x[1],reverse=True)
highestProfit = rev[0:3]
print(highestProfit)
print("Highest profit sold items :")
for j in highestProfit:
    print(f'{list(items)[j[0]]}:{j[1]}')