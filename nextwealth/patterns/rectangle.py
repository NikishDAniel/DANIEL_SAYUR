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
#defining the function
def drawPattern(row,column):
    #looping through the row 
    for i in range(row):
        #if the row is 1 here i.e 0 , and last row print full stars
        if i == 0 or i == (row-1):
            print("* "*column)
        else:
            print("* "+" "*(column-2)*2+"*")
        
row , column = int(input("Enter the number of rows : ")) , int(input("Enter the number of column : "))
drawPattern(row,column)  

'''
output 1 --
Enter the number of rows : 8
Enter the number of column : 8
* * * * * * * * 
*             *
*             *
*             *
*             *
*             *
*             *
* * * * * * * *

'''

'''
output 2 --
Enter the number of rows : 6
Enter the number of column : 9
* * * * * * * * * 
*               *
*               *
*               *
*               *
* * * * * * * * *
'''


'''
output 3 --
Enter the number of rows : 10
Enter the number of column : 10
* * * * * * * * * * 
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
* * * * * * * * * * 

'''