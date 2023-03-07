'''1. Print the level of the password security and if the password is acceptable
    Weak - only alphabets or only numbers or only special chars
    Ok - at least one alphabet, one number and one special char
    strong - at least three alphabets, two numbers and one special char
    Very strong - same as strong, but at least 16 count

    All passwords must be at least 8 chars long. You can use RegEx if you want.'''


#password_level:
#getting input as password variable
password = input("Enter your password with atleast 8 characters:")

#creating lists that needed to check the password word by word
list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
list2 = ['0','1','2','3','4','5','6','7','8','9']       # list for numbers 
list3 = ['`','~','!','@','#','$','%','^','&','*','-','_','+','?']       # list for special characters

# created a variables to store the count of the characters
alphabet_count = 0 
number_count = 0
special = 0
# finding the length of the password that entered as input
length = len(password)
if length >= 8:
# spliting the password string into characters
    for i in password:
        # if the character value is in the list1 count is increases
        if i in list1:
            alphabet_count += 1
        # if the character is in the list2 count is increased   
        elif i in list2:
            number_count += 1
        # it checks fir special characters and increament the count   
        elif i in list3:
            special += 1
    # printing the count of the numbers , characters , special characters in password      
    print("Alphabet :",alphabet_count)
    print("Number :",number_count)
    print("Special :",special)
    # checking the password is weak or okay or strong
    if ( alphabet_count == 8 or number_count ==8 or special == 8 ):
        print("Your password is weak .")
    elif ( alphabet_count >= 3 and number_count >=2 and special >= 1 ):
        if length >= 16:
            print("Your password is very strong")
        else:
            print("Your password is strong")
    elif ( alphabet_count >= 1 and number_count >= 1 and special >= 1 ):
        print("Your password is ok .")
else:
    print("Please enter the password that is greater than 8 characters")