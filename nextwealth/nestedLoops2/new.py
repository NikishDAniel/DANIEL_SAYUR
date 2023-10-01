'''
Get the list of employee names from the user.
Get the monthly phone sales for each employee for the first 4 months of the year.
Sort the employees by name in alphabetical order and for each employee sort their phones sales in 
ascending order.

Eg - Sam, Adam, Sara
Sam's sales - 300, 567,234,1000
Adam's Sales - 340, 456,456,234
Sara' Sales - 1000,234,3000,2000

Output sample
Adam - 456,456,340,234
Sam - ...
Sara - ...

'''
employeeList = []
numberOfEmployees = int(input("Enter the number of employees : "))
for employee in range(1,numberOfEmployees+1):
    inputNames = input(f"Enter the name of employee number {numberOfEmployees} : ")
    employeeList.append(inputNames)
    