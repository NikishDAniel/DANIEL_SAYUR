#Fill in the missing code whereever it says #FillinMissingCode
#Fix the syntax errors as needed.

#This is code has functions for basic arithmetic operations. Add, subtract, multiply and divide
#The main function adds all student marks and finds the average


# function to add 2 numbers
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

#Get 5 marks from student and find the total
total = 0
numberOfSubjects = 5  
#looping through the each subjects     
for i in range(1,numberOfSubjects+1):
    mark = int(input(f"Enter mark {i}: "))
    total = addTwoNumbers(total,mark)
print("Total : ",total)
avg = divide(total,numberOfSubjects)
print("The avg mark is ", avg)



'''
output --

Enter mark 1: 88
Enter mark 2: 54
Enter mark 3: 77
Enter mark 4: 44
Enter mark 5: 65
Total :  328
The avg mark is  65.6

'''