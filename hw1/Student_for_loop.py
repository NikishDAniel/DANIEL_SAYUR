#This is a program to find total marks taken by a student
no_of_students=int(input("Enter the number of students in the class:"))
pass_mark=35
for i in range(1,no_of_students+1):
    #begin of loop
    print("Student count number :",i)
    #getting marks as the input from the user
    Tamil_mark=float(input("Enter your mark in Tamil:"))
    English_mark=float(input("Enter your mark in English:"))      
    Maths_mark=float(input("Enter your mark in Maths:"))
    Science_mark=float(input("Enter your mark in Science:"))
    Social_mark=float(input("Enter your mark in Social:"))
    #Total mark calculation
    Total_Mark=Tamil_mark+English_mark+Maths_mark+Science_mark+Social_mark
    #Printing the total marks
    print("Total marks =",int(Total_Mark))
    #
    if (Tamil_mark >= pass_mark and English_mark >= pass_mark and Maths_mark >= pass_mark and Science_mark >= pass_mark and Social_mark >= pass_mark):
        print("you have passed")
    else:
        print("you failed")
    #end of loop
