'''1. Get the marks for 10th stundet's math paper from 5 different exams. Calculate the average values. 
Calcualte if the student got A grade (avg > 90) or B grade (avg > 80) or C grade (avg > 70) or fail.'''


no_different_exams=5
average=0
maths_1 =float(input("enter your maths mark 1 :"))
maths_2 =float(input("enter your maths mark 2 :"))
maths_3 =float(input("enter your maths mark 3 :"))
maths_4 =float(input("enter your maths mark 4 :"))
maths_5 =float(input("enter your maths mark 5 :"))
average=maths_1+maths_2+maths_3+maths_4+maths_5/no_different_exams
print(average)
if average > 90:
    print("you got A grade")
elif average > 80:
    print("you got B grade")
elif average > 70:
    print("you got C grade")
else:
    print("sorry you failed")

