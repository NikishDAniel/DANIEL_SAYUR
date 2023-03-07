'''2. Same as above. Do the grade avg for all the students in one class. Also, calculate the class average.'''

no_students=int(input("Enter number of students in your class : "))
no_different_exams=5
average=0
avrag=0
class_average=0
for i in range(1,no_students+1):
    
    maths_1 =int(input("enter your maths mark 1 :"))
    maths_2 =int(input("enter your maths mark 2 :"))
    maths_3 =int(input("enter your maths mark 3 :"))
    maths_4 =int(input("enter your maths mark 4 :"))
    maths_5 =int(input("enter your maths mark 5 :"))
    average=(maths_1+maths_2+maths_3+maths_4+maths_5)/no_different_exams
    avg=print(f"Average for {i}: {int(average)}")
    if average > 90:
        print("you got A grade")
    elif average > 80:
        print("you got B grade")
    elif average > 70:
        print("you got C grade")
    else:
        print("sorry you failed")
    t=average
    avrag+=t
    average=0
class_average=avrag/no_students
print(f"Your class got {class_average} percent average")
