######## Problem 3  ###############
#Write a program that prints out a diamond shape using #.
# Hint - print(5 * "$") will print  - $$$$$
# Hint - print(5* "$ ") will print  - $ $ $ $ $
numberOfRows = int(input("Enter the number of rows: "))

#print the top triangle
for row in range(numberOfRows):
    print(" "*(numberOfRows-row-1) + "# "*(row+1)) 
    # if the loop i is comes to the row 
    if row == (numberOfRows-1):
        for row in range(numberOfRows-1):
            print(" "*(row+1) + "# "*(numberOfRows-row-1))
#FillinMissingCode for drawing the bottom triangle

'''
output 1 --
Enter the number of rows: 5
    #
   # #
  # # #
 # # # #
# # # # #
 # # # #
  # # #
   # #
    #
'''

'''
output 2 --
Enter the number of rows: 7
      # 
     # #
    # # #
   # # # #
  # # # # #
 # # # # # #
# # # # # # #
 # # # # # #
  # # # # #
   # # # #
    # # #
     # #
      #
'''