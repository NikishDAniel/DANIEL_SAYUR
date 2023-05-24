########## Problem 3 ############
#Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 white bags (each Rs 1500)
#Customers can buy one or more bags at a time.
#The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
#Display total sales and total number of bags sold

#initialize variables

totalSales , totalBagsSold = 0 , 0
def ordered(customerInput):
    ordered = customerInput.split()
    totalCost = 0
    totalCount = 0
    for order in ordered:
        if order.isdigit():
            count = int(order)
            totalCount += count
        if order.isalpha():
            if order == 'red':
                cost = 100
                totalCost += count*cost
            elif order == 'white':
                cost = 200
                totalCost += count*cost
            else:
                pass
    return totalCost , totalCount

while (totalSales <= 10000) :
    customerInput = input("Enter the number of bags you want to buy : ")
    #FillinMissingCode
    lisy = list(ordered(customerInput))
    totalSales += lisy[0]
    totalBagsSold += lisy[1]
    if totalBagsSold > 10 :
        break
print ( f'Totally {totalBagsSold} sold and total sales {totalSales}') 