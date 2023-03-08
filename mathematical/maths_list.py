'''1. Get the marks for 10th stundet's math paper from 5 different exams. Calculate the average values. 
Calcualte if the student got A grade (avg > 90) or B grade (avg > 80) or C grade (avg > 70) or fail.'''

no_different_exams=int(input("Enter how many different exams in maths :"))
average=0
maths=[]
for i in range(1,no_different_exams+1):
    math = int(input(f"Enter your maths mark {i} :"))
    maths.append(math)
    average = sum(maths)/no_different_exams
print(average)
print(maths)
if average > 90:
    print("you got A grade")
elif average > 80:
    print("you got B grade")
elif average > 70:
    print("you got C grade")
else:
    print("sorry you failed")
