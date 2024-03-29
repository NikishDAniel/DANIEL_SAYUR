# next pattern is - empty diamond

# defining a function
def drawingEmptyDiamond(lines):
    #looping through the line values from 1 to lines
    for i in range(lines):
        # condition that checks the i value is 2 and lines -1 if it is , it means there is spaces
        if i < 2 or i > lines*2-(lines-2):
            print(" "*(lines-i-1) + "# "*(i+1)) 
        
        # conditions for the first row and no spaces
        elif i >= 3 or i <=lines-3:
            print(" "*(lines-i-1)+"# "+" "*(i-3+2)*2+"#")
        # lower part of the diamond
    for i in range(lines-1):
        # if i is less than there will be spaces
        if i < lines-3:
            print(" "*(i+1)+"# "+"  "*(lines-i-3)+"#")
        # else no spaces
        elif i > lines-(lines-1):
            print(" "*(i+1) + "# "*(lines-i-1))
#function call
drawingEmptyDiamond(lines=int(input("Enter the number of lines : ")))

'''output 1 --
Enter the number of lines : 5
    # 
   # #
  #   #
 #     #
#       #
 #     #
  #   #
   # #
    # 
'''

'''output 2 --
Enter the number of lines : 10
         # 
        # #
       #   #
      #     #
     #       #
    #         #
   #           #
  #             #
 #               #
#                 #
 #               #
  #             # 
   #           #
    #         #
     #       #
      #     #
       #   #
        # #
         #
'''

'''
output 3 ---
l/Desktop/DANIEL_SAYUR/nextwealth/patterns/emptyDiamond.py"
Enter the number of lines : 8
       #        
      # #       
     #   #      
    #     #     
   #       #    
  #         #   
 #           #  
#             # 
 #           #  
  #         #   
   #       #    
    #     #     
     #   #      
      # #       
       #    
'''