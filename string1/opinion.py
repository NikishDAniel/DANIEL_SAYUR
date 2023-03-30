''' 1. Take an opinion poll among students. Ask the students whether they like online class
 (input as 1), in person class (input as 2) or mixed (input as 3).
 Display the percentage of the female students that like online classes.
  You can end the poll when someone answers ‘No comment (input as 4)’ or when the poll 
  reaches at least 10 students.'''

#assigning the values to the variables
no_of_opinion = 10
no_of_females = 0
no_of_females_liked = 0

# creating a list for storing the multiple ways of giving inputs by the users 
a=["female","Female","FEMALE"]
b=["male","Male","MALE"]

#using looping for repeating the same step
for i in range (1,no_of_opinion+1):
    print( f"poll : {i}")       # this line is to show user the count of the poll
    gender=input("Enter your gender :")
    print("1. Online class ")    #getting inputs
    print("2. Offline class ")
    print("3. Mixed class ")
    print("4. No Comments ")
    option=int(input("Enter your choice :"))            #asking user to enter the choice they  want 
    
    if gender in a:
        no_of_females += 1
        if (option == 1 and gender in a):
            no_of_females_liked += 1                    #this is to take count of females who like online classes
            no_of_opinion += 1
    elif option == 1 and gender in b:
            no_of_opinion += 1
            no_of_females += 1
    elif option == 2:
        no_of_opinion += 1
    elif no_of_opinion == 3:
        no_of_opinion += 1
    elif option == 4:
        break
    else:
        print("Enter the valid option.")            #if the choice is not in the either the above options
if no_of_females <=0:
    print("There is no female student till attended the poll.")
else:
    percentage = (no_of_females_liked/no_of_females)*100
    print(f"{percentage}% of female students like online classes.")
