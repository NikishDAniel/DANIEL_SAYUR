############## Problem 4 ##############
#Calculate the Grade for a student, using 3 marks.
# The student has 100 marks in any one subject, Grade is A.
# if the student has 90 or above in any one subject  Grade is B
# if the student has 60 or above in any one subject  Grade is C
# if the student has 50 or less  in all subjects  Grade is F, otherwise Grade is D.

#Code

#getting marks
mark1 = int(input("Enter the mark 1 : "))
mark2 =int(input("Enter the mark 2 : "))
mark3 = int(input("Enter the mark 3 : "))

#at leasr one mark is 100
if(mark1 == 100 or mark2 == 100 or mark3 == 100): 
    print ("Grade A")
    
#90 or above in any one subject
elif (mark1 >= 90 or mark2 >= 90 or mark3 >= 90): 
    print ("Grade B")
    
#60 or above in any one subjec
elif (mark1 >= 60 or mark2 >= 60 or mark3 >= 60):
    print("Garde C")
    
#50 or less  in all subjects
elif (mark1 <= 50 and mark2 <= 50 and mark3 <= 50):
    print ("Grade F")
    
#otherwise part
else:
    print ("Grade D")


'''
output ---
Enter the mark 1 : 45
Enter the mark 2 : 100
Enter the mark 3 : 89
Grade A

'''