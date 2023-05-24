#Write code for drawing these patterns.
#Get width and length from the user.
# draw a empty rectangle woth char *
#eg 
'''
Row 5, col 7
* * * * * * *
*           *
*           *
*           *
* * * * * * *

'''
def rectangle(row,column):
    for i in range(row):
        if i == 0 or i == (row-1):
            print("* "*column)
        else:
            print("* "+" "*(column-2)*2+"*")
        
row , column = int(input("Enter the number of rows : ")) , int(input("Enter the number of column : "))
rectangle(row,column)  
