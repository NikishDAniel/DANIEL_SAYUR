# here the problem is to find and the factorial

'''
define a functions '''



#factorial function
def findfactorial(numbers):
    
    # assigning the result variable and assign it to 0
    result = 1
    
    # looping through the number 
    for number in range(2,numbers+1):       
        result =  result*(number)
    # returning the result
    return result

#function call
print(findfactorial(int(input())))
