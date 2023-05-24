######## Problem  2 ###############
#Print multiplication tables from 7 to 16, each number upto 12 rows.
def multiplication(number1,number2):
  answer = number1*number2
  print(f'{number1} x {number2} = {answer}')

number1 = int(input("Enter the first number : "))
number2 = int(input("Enter the second number : "))
numberOfRows = int(input("Enter the row number :"))
for num1 in range(number1,number2+1):
  for num2 in range(1,numberOfRows+1):
    multiplication(num1,num2)
  print(end="-------------------\n")
