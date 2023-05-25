############ Problem 2 ####
#Calculate the BMI and if the person is underweihgt/normal/overweight/obese
#Google how to calculate BMI and decide on the input.

#a function to print the result
def result(bmi):
    
    # if elif else for the conditions
    if bmi <18.5:
        return "Underweight"
    elif bmi >18.5 and bmi < 24.9:
        return "Normal"
    elif bmi >25.0 and bmi < 39.9:
        return "Overweight"
    elif bmi >= 40.0 :
        return "Obese"
    
#a function to calculate the bmi
def calculateBMI(weight,height):
    bmi = weight/height**2
    return bmi

# getting input
weight = float(input("Enter your weight in KGs : "))
height = float(input("Enter your height in meters : "))

#calling the function and storing the returning value from the respective functions
bmi = calculateBMI(weight,height)
print(f'You are BMI is {abs(bmi)}')
print(f'You are {result(bmi)}')



'''
output 1 --

Enter your weight in KGs : 50
Enter your height in meters : 1.7
You are BMI is 17.301038062283737
You are Underweight
'''

'''
output 2 --
Enter your weight in KGs : 65
Enter your height in meters : 1.8
You are BMI is 20.061728395061728
You are Normal
'''