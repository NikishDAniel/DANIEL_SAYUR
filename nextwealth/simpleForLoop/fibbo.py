######## Problem 2 ###############
#Write a program that prints out the Fibonacci sequence up to a given number.
#example 1,1,2,3,5,8 , next number is the sum of previous two numbers.
def fibonacci(number):
    startNumber = 0
    secondNumber= 1
    print(startNumber,secondNumber,end=' ')
    for numbers in range(1,number-1):
        result = secondNumber+ startNumber
        print(result,end=" ")
        startNumber = secondNumber
        secondNumber = result 
fibonacci(number=int(input("Enter the number : "))) 