def addTwoNumbers(n1, n2):
    sumanswer = n1 + n2
    # returning sum of two numbers
    return sumanswer
# function to sub 2 numbers
def subtractAfromB(a, b):
    subtractAnswer = abs(a - b)
    return subtractAnswer
# function to mul 2 numbers
def multiplyTwoNumbers(n1,n2):
    multiplyAnswer = (n1*n2)
    return multiplyAnswer

# function to divide
def divide(numerator, denominator):
    dividedanswer = numerator / denominator
    return dividedanswer
#main code
def sum(i):
    total =0
    for num in i:
        total = addTwoNumbers(total,num)
    return total

#we have sales data for a week. 
costOfCoffee, costOfTea, costOfVadai =25,20,25
list1 = []
coffeeSales = [56,78,56,45,90, 103,120]
teaSales = [100,123,456,123,222,400,346]
vadaiSales = [23,45,67,12,89,90,120]
list1.append(coffeeSales)
list1.append(teaSales)
list1.append(vadaiSales)
#Find total sales in the week.
total =0
for i in list1:   
    output = sum(i)
    total = addTwoNumbers(total,output)
    avg =divide(output,len(i))
    print(f'The total sales is {output} , and its their average is {avg} ')   
employeeSalary = 500 #Rs500 per day
employeeSalaryPerWeek = multiplyTwoNumbers(500,7)
#calculate sales per week
print(f"the total sales per week is {total}")
#calcuate sales per month
salesPerMonth = multiplyTwoNumbers(total,4)
print(f"Total sales per month : ",salesPerMonth)
#calculate profit.
print(f'Profit is :', subtractAfromB(salesPerMonth,employeeSalary))


'''
output --
The total sales is 548 , and its their average is 78.28571428571429 
The total sales is 1770 , and its their average is 252.85714285714286 
The total sales is 446 , and its their average is 63.714285714285715
the total sales per week is 2764
Total sales per month :  11056
Profit is : 10556

'''