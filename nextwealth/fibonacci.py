'''fibb'''

#getting input
number = int (input("Enter the number : "))  
firstNumber = 0
secondNUmber = 1
print(firstNumber,secondNUmber,end=" ")
#looping for the number
for num in range(1,number-1):
    result = firstNumber + secondNUmber
    print(result,end=" ")
    firstNumber = secondNUmber
    secondNUmber = result
    
'''
output 1 --
Enter the number : 7
0 1 1 2 3 5 8  
'''

'''
output 2 --
Enter the number : 23
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711
'''

'''
output 3 --
Enter the number : 17
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
'''