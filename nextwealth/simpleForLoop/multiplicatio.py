######## Problem 1 ###############
#write multiplication table like this
# 1 * 1 = 1
# 1 * 2 = 2
#etc. Get the number as input

multiplicationNumber = int (input("Enter the number to multiply: "))
noOfEntries = int (input("How many rows do you want to print : "))
# loop through number of entries
for i in range (1,noOfEntries+1):
    print (f'{multiplicationNumber} * {i} = {multiplicationNumber*i}')
           
'''
output 1 --
Enter the number to multiply: 8
How many rows do you want to print : 4
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32

'''

'''
output 2 --
Enter the number to multiply: 5
How many rows do you want to print : 15
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
5 * 11 = 55
5 * 12 = 60
5 * 13 = 65
5 * 14 = 70
5 * 15 = 75'''