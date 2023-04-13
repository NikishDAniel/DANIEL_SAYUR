'''Write a Python program to find those numbers which are divisible by 7 and multiples of 5, 
between 1500 and 2700 (both included)'''

'''
    -- defininig the function to get the range between the two input numbers
    -- define another function to append the divisible number 
    -- return the list
'''
#def numberBetween(number1,number2):
NumberBetween = []
def listAppend(k):
    NumberBetween.append(k)
    return NumberBetween
def multipleOf(number1,number2):
    for i in range(number1,number2+1):
        if (i % 7 == 0 or i % 5 == 0):
            output = listAppend(i)
    return output 
number = multipleOf(int(input("Enter the first number :")),int(input("Enter the second number :")))
print(number)
