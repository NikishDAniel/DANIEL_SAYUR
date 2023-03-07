'''2. Check if the username and password is correct. 
     Username should contain the char @  and '.com' or '.edu' or '.tech' or '.org' at the end.
     password is the first, third, and last 3 letters of the username followed by the first three letters of the 
     name of the company mentioned in the username, followed by any 3 numbers.
     eg username : myname@sayur.com. password - mnamesay123'''

# getting input from the user to enter their username and password
user_name = input("Enter your user_name: ")

# creating the list for checking the numbers at the password checking
li1 = ['0','1','2','3','4','5','6','7','8','9']

# assigning a variable named at to represent the symbol '@'
symbolAt='@'

# list for checking the user name is ending with finished with the listed values
li=[".com",'.edu','.tech','.org']

if symbolAt in user_name and (user_name.endswith(".com") or user_name.endswith(".edu") or user_name.endswith(".tech") or user_name.endswith(".org")):
    print("Your user name is ok.")
else :
    print(f"Please enter username with '{symbolAt}' and it must ends with {li}")


# here defining a function to check the validity of the password
def password_check(password):
    length = user_name.find('@')
    if symbolAt in user_name:     
        firstLetter = password[0]
        first_1 = user_name[0]
        second = password[1]        
        second_1 = user_name[2]
        three = password[2:5]
        three_1 =user_name[length - 3:length]      
        four = password[5:8]
        four_1 = user_name[length + 1:length + 4]
        if (firstLetter == first_1 and second == second_1 and three == three_1 and four == four_1 ):
            number_1 = password[8:11]
            for i in number_1:
                if i in li1:
                    break
                else:
                    print("Please enter numbres at last")
            print("Your password is ok.")
        else:
            print("Please re-enter your password ")
password_check(input("Enter your password :"))

    
        




