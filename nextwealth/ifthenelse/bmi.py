############ Problem 2 ####
#Calculate the BMI and if the person is underweihgt/normal/overweight/obese
#Google how to calculate BMI and decide on the input.
def result(bmi):
    if bmi <18.5:
        return "Underweight"
    elif bmi >18.5 and bmi < 24.9:
        return "Normal"
    elif bmi >25.0 and bmi < 39.9:
        return "Overweight"
    elif bmi >= 40.0 :
        return "Obese"
def calculateBMI(weight,height):
    bmi = weight/height**2
    return bmi
weight = float(input("Enter your weight in KGs : "))
height = float(input("Enter your height : "))
bmi = calculateBMI(weight,height)
print(f'You are BMI is {abs(bmi)}')
print(f'You are {result(bmi)}')