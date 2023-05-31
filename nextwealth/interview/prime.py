# a function to find prime numbers
def findprime(numbers):
    
    # checking the number is valid or not
    if numbers <= 1:
        return "please enter greater than 1"
    # looping till the input number
    for rangenumbers in range(2,numbers+1): 
        # loops for the possibility check
        for loopingnumber in range(2,numbers+1):  
            # if the rangenumber equals the loopingnumber then the remiander will be zero , so we need to skip this condition             
            if loopingnumber == rangenumbers :
                continue
            
            # if the range number is divisible by number means not a prime number 
            elif rangenumbers % loopingnumber == 0:
                break
        # this else is for the 'for' loop , it gets into this else when the loop runs completely
        else:
                print(rangenumbers , end=' ')

# function call to findprime
findprime(int(input("Enter the number : ")))

