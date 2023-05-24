############# Problem 1 ###########
#Google and find the tax slabs for income tax for India. Write a program to calculate the income tax for an 
#individual. Input is Salary. Optional input - any deductions.
def incomeTax(income):
    if income < 300000:
        return "Nil"
    elif income >= 300000 or income < 600000:
        tax = income*0.05
    elif income >= 600000 or income < 900000:
        taxRate = 15000
        tax += (income*0.1 + taxRate)
    elif income >= 900000 or income < 1200000:
        taxRate = 45000
        tax += (income*0.15 + taxRate)
    elif income >= 1200000 or income <= 1500000:
        taxRate = 90000
        tax += (income*0.2 + taxRate)
    elif income > 1500000 :
        taxRate = 150000
        tax += (income*0.3 + taxRate)
    return tax
salary = float(input("Enter your salary : "))
otherSource = float(input("Enter your any other sources (if no give input as 0): "))
if otherSource == 0:
    income = salary*12
income = salary*12*otherSource
print(f'Your income tax is {incomeTax(income)}')