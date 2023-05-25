######## Problem 2 ###############
#Write a program that prints out the Fibonacci sequence up to a given number.
#example 1,1,2,3,5,8 , next number is the sum of previous two numbers.

# defining a function to return the fibonacci sequence
def fibonacci(number):
    startNumber = 0
    secondNumber= 1
    print(startNumber,secondNumber,end=' ')
    # looping through the number range
    for numbers in range(1,number-1):
        result = secondNumber+ startNumber
        print(result,end=" ")
        startNumber = secondNumber
        secondNumber = result 
fibonacci(number=int(input("Enter the number : "))) 

'''output 1 --
Enter the number : 7
0 1 1 2 3 5 8 
'''

'''
output 2 --
Enter the number : 21
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
'''