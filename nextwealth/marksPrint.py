######## Problem  1 ###############
# Get and print the 2 marks for 3 students. Also, get each studen't name
# output should be
# Mark 1 for Student 1 is 55
# Mark 2 for Student 1 is 67
# Mark 1 for Student 2 is 56 
#etc
'''
studentsMarks = []
students = []  
numberOfSubjects = 2
studentsCount = 0    
for student in range (3):
    studentName = input()
    students.append(studentName)
    for mark in range (numberOfSubjects):
        inputMark = int(input()) #use formatted string
        studentsMarks.append(inputMark)
for aStudent in students:
    for marks in range(numberOfSubjects):
        print(f'Mark {marks+1} for student {aStudent} is {studentsMarks[0]}')
        studentsMarks.remove(studentsMarks[0])'''
        
        
        
studentsMarks = []
students = []  
numberOfSubjects = 2
studentsCount = 0    
for student in range (3):
    studentName = input()
    students.append(studentName)
    for mark in range (numberOfSubjects):
        inputMark = int(input())
        studentsMarks.append(inputMark)
for aStudent in students:
    stir = ''
    for marks in range(numberOfSubjects):
        stir += " "+str(studentsMarks[0])
        studentsMarks.remove(studentsMarks[0])
    print(f'Mark obtained by student {aStudent} is {stir}')
        