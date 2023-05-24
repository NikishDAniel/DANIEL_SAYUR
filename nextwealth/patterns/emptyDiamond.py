# next pattern is - empty diamond
def emptyDiamond(lines):
    for i in range(lines):
        if i < 2 or i > lines*2-(lines-2):
            print(" "*(lines-i-1) + "# "*(i+1)) 
        elif i >= 3 or i <=lines-3:
            print(" "*(lines-i-1)+"# "+" "*(i-3+2)*2+"# ")
        if i == (lines-1):
            for i in range(lines-1):
                if i < lines-3:
                    print(" "*(i+1)+"# "+"  "*(lines-i-3)+"# ")
                elif i > lines-(lines-1):
                    print(" "*(i+1) + "# "*(lines-i-1))
emptyDiamond(lines=int(input("Enter the number of lines : ")))