'''#write code for both for and while loop
#Get marks from 5  students and calculate avg'''
#
def average():
#for loop
    total = 0
    for i in range(1,6):
        mark = int(input(f"Enter the mark of {i} subject : "))
        #get user input
        #FillinMissingCode
        total += mark
    return total

#using while loop
total = 0
noOfStudents = 5
i = 0
while (i < noOfStudents):
    print(f"student {i+1}:")
    #get user input
    mark = average()
    #FillinMissingCode
    total += mark
    average = total/noOfStudents
    i += 1
print ("Average is ",  average)