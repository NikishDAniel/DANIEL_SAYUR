######## Problem 1 ###############
#Write a program that prints out a diamond shape using $.
#After printing each line, wait for user input. If the user presses space, continue
#If the users presses any other key, stop printing. Maximum 10 lines

def diamond(lines):
    for i in range(lines):
        print(" "*(lines-i-1) + "$ "*(i+1)) 
        key = input() 
        if ord(key) != 32:
            break       
        if i == (lines-1):
            for i in range(lines-1):
                print(" "*(i+1) + "$ "*(lines-i-1))
                key2 = input()
                if ord(key2) != 32:
                    break                 
                elif ord(key2) == 32:
                    continue
        
        elif ord(key) == 32:
            continue
    
lines = int(input("Enter the number of rows : "))
if (lines > 10):
    lines = 10
diamond(lines)