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
'''

list = [maths,science , history]
for i in list: maths[]
for j in maths:


'''
marksInMaths = [56,78,56,45,90]
for marks in marksInMaths:
    totalMathsMark = addTwoNumbers(totalMathsMark,marks)
dividedOutput1 = divide(totalMathsMark,len(marksInMaths))   
print(dividedOutput1)


marksInScience = [90,78,67,8,98] 
for marks in marksInScience:
    totalScienceMark = addTwoNumbers(totalScienceMark,marks)
dividedOutput2 = divide(totalScienceMark,len(marksInScience))   
print(dividedOutput2) 

marksInHistory = [87,44,56,34,90]
for marks in marksInHistory:
    totalHistoryMark = addTwoNumbers(totalHistoryMark,marks)
dividedOutput3 = divide(totalHistoryMark,len(marksInHistory))   
print(dividedOutput3) 
three.append(dividedOutput1) 
three.append(dividedOutput2) 
three.append(dividedOutput3) 
#Call divide function to get the average from all three subjects
#FillinMissingCode
threeSubTotal = 0
for marks in three:
    threeSubTotal = addTwoNumbers(threeSubTotal,marks)
avg = divide(threeSubTotal,len(three))
print("The avg mark is ", avg)