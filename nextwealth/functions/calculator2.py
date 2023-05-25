#same calculator


#defining a function to add two numbers
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
three = []
totalMathsMark = 0
totalScienceMark = 0 
totalHistoryMark = 0

marksInMaths = [56,78,56,45,90]
for marks in marksInMaths:
    totalMathsMark = addTwoNumbers(totalMathsMark,marks)
dividedOutput1 = divide(totalMathsMark,len(marksInMaths))   
print("The average is :",dividedOutput1)


marksInScience = [90,78,67,8,98] 
for marks in marksInScience:
    totalScienceMark = addTwoNumbers(totalScienceMark,marks)
dividedOutput2 = divide(totalScienceMark,len(marksInScience))   
print("The average is :",dividedOutput2) 

marksInHistory = [87,44,56,34,90]
for marks in marksInHistory:
    totalHistoryMark = addTwoNumbers(totalHistoryMark,marks)
dividedOutput3 = divide(totalHistoryMark,len(marksInHistory))   
print("The average is :",dividedOutput3) 
three.append(dividedOutput1) 
three.append(dividedOutput2) 
three.append(dividedOutput3) 
#Call divide function to get the average from all three subjects
#FillinMissingCode
threeSubTotal = 0
for marks in three:
    threeSubTotal = addTwoNumbers(threeSubTotal,marks)
avg = divide(threeSubTotal,len(three))
print("The total avg mark is ", avg)

'''
output --
 daniel/Desktop/DANIEL_SAYUR/nextwealth/functions/calculator2.py"
The average is : 65.0
The average is : 68.2
The average is : 62.2
The total avg mark is  65.13333333333333

'''