########## Problem 3 ############
#Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 white bags (each Rs 1500)
#Customers can buy one or more bags at a time.
#The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
#Display total sales and total number of bags sold

#initialize variables
totalSales , totalBagsSold = 0 , 0

#function to calculate the ordered items
def ordered(customerInput):
    ordered = customerInput.split()
    totalCost = 0
    totalCount = 0
    count = 0
    #looping through the ordered items
    for order in ordered:
        # if the index is number add it on the count
        if order.isdigit():
            count = int(order)
            totalCount += count
        # if it is letters then check for  red or white 
        if order.isalpha():
            # red bag code
            if order == 'red':
                cost = 100
                totalCost += count*cost
            # white bag code
            elif order == 'white':
                cost = 200
                totalCost += count*cost
            # if the words are not red and white then pass
            else:
                pass
    return totalCost , totalCount

#loop to check for the total cost and breaking when the loop when needed
while (totalSales <= 10000) :
    customerInput = input("Enter the number of bags you want to buy : ")
    #FillinMissingCode
    listOfReturn = list(ordered(customerInput))
    totalSales += listOfReturn[0]
    totalBagsSold += listOfReturn[1]
    
    # if total bags sold greater than 10 then break
    if totalBagsSold > 10 :
        break
print ( f'Totally {totalBagsSold} sold and total sales {totalSales}') 

'''output 1 --
Enter the number of bags you want to buy : 5 red and 4 white
Enter the number of bags you want to buy : 5 red and 4 white
Totally 18 sold and total sales 2600
'''

'''
output 2 --
Enter the number of bags you want to buy : 7 red
Enter the number of bags you want to buy : 4 white
Totally 11 sold and total sales 1500
'''