######## Problem  3 ###############
#Print Chess board (alternate black and white squares)
#print('\u25A0') - will print white Square. You can use "B" to print black squares
def chessBoard():
    for i in range(8):
        for j in range(8):
            if i % 2 == 0 and j%2 == 0:
                print("B",end=' ')
            elif i % 2 == 1 and j%2 == 1:
                print("B",end=' ')
            else:
                print('\u25A0',end=' ')
        print()
print("------CHESS BOARD------")
chessBoard()