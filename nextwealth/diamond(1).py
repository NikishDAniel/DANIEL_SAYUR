######## Problem 3  ###############
#Write a program that prints out a diamond shape using #.
# Hint - print(5 * "$") will print  - $$$$$
# Hint - print(5* "$ ") will print  - $ $ $ $ $
n = int(input("Enter the number of rows: "))

#print the top triangle
for i in range(n):
    print(" "*(n-i-1) + "# "*(i+1)) 
    if i == (n-1):
        for i in range(n-1):
            print(" "*(i+1) + "# "*(n-i-1))
#FillinMissingCode for drawing the bottom triangle



