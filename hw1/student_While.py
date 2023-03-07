no_of_students=int(input("Enter the number of students in the class:"))
pass_mark=35
while no_of_students!=0 and no_of_students>0:
    Tamil_mark=float(input("Enter your mark in Tamil:"))
    English_mark=float(input("Enter your mark in English:"))
    Maths_mark=float(input("Enter your mark in Maths:"))
    Science_mark=float(input("Enter your mark in Science:"))
    Social_mark=float(input("Enter your mark in Social:"))
    Total_Mark=Tamil_mark+English_mark+Maths_mark+Science_mark+Social_mark
    print("Total marks =",int(Total_Mark))
    no_of_students-=1
    if ( Tamil_mark >= pass_mark and English_mark >= pass_mark and Maths_mark >= pass_mark and Science_mark >= pass_mark and Social_mark >= pass_mark ):
        print("you have passed")
    else:
        print("you failed")