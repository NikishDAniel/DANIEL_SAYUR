'''1. Write an app for a cafe. Decide on the items in the cafe, stock of each item in the morning, 
stock in the evening, sales amount at the end of the day and profit for each item. You need to restock an item 
if the supply reaches 20% of the stock. Print the 3 items with highest sales, and top 3 highest profit.
Fruit stall - Mango, Apple, Banana

Fruit Inventory list = 20, 30, 25
Fruit Min = 5, 10,8
Fruit reorder = 10, 10, 10
IN a loop, get the input from customer
based on the fruit and quantity, fill the order and reorder if necessary
at the end print current inventor'''

'''Plan:
    -- ask user what they want
    -- check for that particular item'''


# creating the necessary list
listOfFruits = ['Mango', 'Apple', 'Banana']
inventoryList = [20,30,25]
minItems = [5,10,8]
listReorder = [10,10,10]
customer = 0 
customerLimit = 5

while customer <= customerLimit:
    print(f"customer {customer} :")
    input("What do you want ?")

def fruitsCheck(listOfFruits,):