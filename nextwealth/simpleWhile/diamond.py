######## Problem 1 ###############
#Write a program that prints out a diamond shape using $.
#After printing each line, wait for user input. If the user presses space, continue
#If the users presses any other key, stop printing. Maximum 10 lines


# a function to draw the diamond pattern
def diamond(lines):
    # looping through each roe
    for row in range(lines):
        print(" "*(lines-row-1) + "$ "*(row+1)) 
        key = input() 
        # if the input pressed is space then break it
        if ord(key) != 32:
            break   
        
        #bottom part    
        if row == (lines-1):
            # looping for the rows 
            for row in range(lines-1):
                print(" "*(row+1) + "$ "*(lines-row-1))
                key2 = input()
                # same as the above if space then
                if ord(key2) != 32:
                    break                 
                elif ord(key2) == 32:
                    continue
        
        elif ord(key) == 32:
            continue
    
lines = int(input("Enter the number of rows : "))
#checking and assigning the lines = 10 if true
if (lines > 10):
    lines = 10
diamond(lines)

'''
output1 --
Enter the number of rows : 5
    $ 
 
   $ $ 
 
  $ $ $ 
 
 $ $ $ $ 
 
$ $ $ $ $ 
 
 $ $ $ $ 
 
  $ $ $ 
 
   $ $ 
 
    $ 
'''

'''output 2 --
Enter the number of rows : 10
         $ 
 
        $ $ 
 
       $ $ $ 
 
      $ $ $ $ 
 
     $ $ $ $ $ 
 
    $ $ $ $ $ $ 
s

'''