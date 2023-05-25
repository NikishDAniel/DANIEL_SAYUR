############# Problem 1 ###########
#Google and find the tax slabs for income tax for India. Write a program to calculate the income tax for an 
#individual. Input is Salary. Optional input - any deductions.

#function to calculate the incomeTax and return the tax amount
def incomeTax(income):
    tax = 0 
    # if then elif for each conditions
    if income < 300000:
        return "Nil"
    elif income >= 300000 and income < 600000:
        tax = income*0.05
    elif income >= 600000 and income < 900000:
        taxRate = 15000
        tax += (income*0.1 + taxRate)
    elif income >= 900000 and income < 1200000:
        taxRate = 45000
        tax += (income*0.15 + taxRate)
    elif income >= 1200000 and income <= 1500000:
        taxRate = 90000
        tax += (income*0.2 + taxRate)
    elif income > 1500000 :
        taxRate = 150000
        tax += (income*0.3 + taxRate)
    return tax

# getting salary as input
salary = float(input("Enter your salary : "))
# any other sources of income
otherSource = float(input("Enter your any other sources (if no give input as 0): "))

#checking if there is any extra sources
if otherSource == 0:
    income = salary*12
income = salary*12+otherSource
print(f'Your income tax is {incomeTax(income)}')


'''
output 1 --
Enter your salary : 15000
Enter your any other sources (if no give input as 0): 0
Your income tax is Nil

'''

'''
output 2 --
Enter your salary : 100000
Enter your any other sources (if no give input as 0): 2000
Your income tax is 330400.0
'''