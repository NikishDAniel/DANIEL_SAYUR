# next pattern is - empty diamond

# defining a function
def drawingEmptyDiamond(lines):
    #looping through the line values from 1 to lines
    for i in range(lines):
        # condition that checks the i value is 2 and lines -1
        if i < 2 or i > lines*2-(lines-2):
            print(" "*(lines-i-1) + "# "*(i+1)) 
        elif i >= 3 or i <=lines-3:
            print(" "*(lines-i-1)+"# "+" "*(i-3+2)*2+"# ")
        # lower part
        if i == (lines-1):
            #looping for the bottom values 
            for i in range(lines-1):
                # if i is less than 
                if i < lines-3:
                    print(" "*(i+1)+"# "+"  "*(lines-i-3)+"# ")
                elif i > lines-(lines-1):
                    print(" "*(i+1) + "# "*(lines-i-1))
#function call
drawingEmptyDiamond(lines=int(input("Enter the number of lines : ")))