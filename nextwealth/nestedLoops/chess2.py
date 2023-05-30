######## Problem  3 ###############
#Print Chess board (alternate black and white squares)
#print('\u25A0') - will print white Square. You can use "B" to print black squares



# initialise the values 
fi = "\u25A0 B "*4
la = "B \u25A0 "*4
print("----CHESS BOARD----")
# loops for each loops 
for rows in range(8):
    
    # printing the first variable if it is even
    if rows %2 == 0:
        print(fi)
    # else printing this 
    else:
        print(la)
        
'''
output ---
----CHESS BOARD----
■ B ■ B ■ B ■ B 
B ■ B ■ B ■ B ■
■ B ■ B ■ B ■ B
B ■ B ■ B ■ B ■
■ B ■ B ■ B ■ B
B ■ B ■ B ■ B ■
■ B ■ B ■ B ■ B
B ■ B ■ B ■ B ■
'''