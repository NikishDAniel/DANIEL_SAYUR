#write code for both for and while loop
#Get marks from 5  students and calculate avg
#


# function to calculate average
def calculateAverage():
#for loop to get marks
    total = 0
    for i in range(1,6):
        mark = int(input(f"Enter the mark of {i} subject : "))
        total += mark
    return total

#using while loop
total = 0
noOfStudents = 5
i = 0
while (i < noOfStudents):
    print(f"student {i+1}:")
    mark = calculateAverage()
    total += mark
    i += 1
calculateAverage = total/noOfStudents
   
print ("Average is ",  calculateAverage)


'''
output --
student 1:
Enter the mark of 1 subject : 74
Enter the mark of 2 subject : 74
Enter the mark of 3 subject : 75
Enter the mark of 4 subject : 75
Enter the mark of 5 subject : 46
student 2:
Enter the mark of 1 subject : 45  
Enter the mark of 2 subject : 77
Enter the mark of 3 subject : 89
Enter the mark of 4 subject : 45
Enter the mark of 5 subject : 69
student 3:
Enter the mark of 1 subject : 48
Enter the mark of 2 subject : 78
Enter the mark of 3 subject : 45
Enter the mark of 4 subject : 78
Enter the mark of 5 subject : 98
student 4:
Enter the mark of 1 subject : 78
Enter the mark of 2 subject : 45
Enter the mark of 3 subject : 89
Enter the mark of 4 subject : 4
Enter the mark of 5 subject : 78
student 5:
Enter the mark of 1 subject : 87
Enter the mark of 2 subject : 97
Enter the mark of 3 subject : 88
Enter the mark of 4 subject : 55
Enter the mark of 5 subject : 44
Average is  336.2'''