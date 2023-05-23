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
marksInMaths = [56,78,56,45,90]
marksInScience = [90,78,67,8,98]
marksInHistory = [87,44,56,34,90]
subMarks = [marksInMaths,marksInScience,marksInHistory]
totalAverage = 0
for i in subMarks:
    totalMark = 0 
    for marks in i:       
        totalMark = addTwoNumbers(totalMark,marks)
    dividedOutput = divide(totalMark,len(i))   
    print("The average is :",dividedOutput)
    totalAverage = addTwoNumbers(dividedOutput,totalAverage)
overAllAvg = divide(totalAverage,len(subMarks))
print("the total average : ", overAllAvg)