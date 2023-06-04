'''
Program 1 - Write a program to print the following pattern.
Input is 5 for the following pattern.
5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5      
5 4 3 2 2 2 3 4 5       
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5
'''

def lowerPart(row,number):
    for col in range(number*2-1):
        if (col == 0) or (col == number*2-2):
            print(number,end=" ")
        else:
            if col==row or (col > row and col <= (2*number-row-2)):
                output += (col - row)
            elif col>number:
                output += 1
            else:
                output = number-col
            print(output,end=' ')
        print() 

def printPattern(number):
    for row in range(number*2-1):
        if (row == 0) or (row == number*2-2):
            print(f'{number} '*(number*2-1))
        elif row >=number:
            lowerPart(row,number)
        else:
            for col in range(number*2-1):
                if (col == 0) or (col == number*2-2):
                    print(number,end=" ")
                else:
                    if row >= 2*(number-1)/2 and col >= 2*(number)/2:
                        output += 1 
                     
                    else:
                        if col==row or (col > row and col <= (2*number-row-2)):
                            output = number-row
                        elif col>number:
                            output += 1
                        else:
                            output = number-col
                    print(output,end=' ')
            print()               
    
printPattern(5)