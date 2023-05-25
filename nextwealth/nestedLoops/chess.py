######## Problem  3 ###############
#Print Chess board (alternate black and white squares)
#print('\u25A0') - will print white Square. You can use "B" to print black squares

#a function to draw the chessboard
def chessBoard():
    # looping through the each row and column
    for row in range(8):
        for column in range(8):
            # if the rows is even and column is also even then print one colour
            if row % 2 == 0 and column%2 == 0:
                print("B",end=' ')
            
            # if row is odd and column is also then print the same colour as the above
            elif row % 2 == 1 and column%2 == 1:
                print("B",end=' ')
            
            #otherwise part
            else:
                print('\u25A0',end=' ')
        print()
print("------CHESS BOARD------")
chessBoard()

'''output --

------CHESS BOARD------
B ■ B ■ B ■ B ■ 
■ B ■ B ■ B ■ B
B ■ B ■ B ■ B ■
■ B ■ B ■ B ■ B
B ■ B ■ B ■ B ■
■ B ■ B ■ B ■ B
B ■ B ■ B ■ B ■
■ B ■ B ■ B ■ B

'''



######## Problem  3 ###############
#Print Chess board (alternate black and white squares)
#print('\u25A0') - will print white Square. You can use "B" to print black squares

#a function to draw the chessboard
def chessBoard():
    # looping through the each row and column
    for row in range(8):
        for column in range(8):
            # if the rows is even and column is also even then print one colour
            if row % 2 == 0 and column%2 == 0:
                print("\u25A0",end=' ')
            
            # if row is odd and column is also then print the same colour as the above
            elif row % 2 == 1 and column%2 == 1:
                print("\u25A0",end=' ')
            
            #otherwise part
            else:
                print('B',end=' ')
        print()
print("------CHESS BOARD------")
chessBoard()
'''output 2 ==

------CHESS BOARD------
■ B ■ B ■ B ■ B
B ■ B ■ B ■ B ■
■ B ■ B ■ B ■ B
B ■ B ■ B ■ B ■ 
■ B ■ B ■ B ■ B
B ■ B ■ B ■ B ■
■ B ■ B ■ B ■ B
B ■ B ■ B ■ B ■'''