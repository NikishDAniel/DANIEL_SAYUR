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
dicti = {
        "(":")",
        '[':']',
        '{':'}',
        ")":"(",
        ']':'[',
        '}':'{'
    }
s = input()
new = s.replace('',' ').split()
for chara in new:
    if dicti[chara] not in new:
        print('false')
        break
    elif dicti[chara] in new and new.count(chara) == new.count(dicti[chara]):
        print('true')