'''THere are two arrays of numbers. the numbers are sorted in ascending order. 
Find the numbers that are common in both arrays. 
Eg - array 1 = [1,3,7,9,13,14], array2 [1,2,7,13,15]. answer - [1,7,13]
'''

''' 
    -- creating lists to compare and creating an empty list
    -- looping through the first array
    -- checking for the same in second list
'''
#initial state
output = []
array1 = [1,3,9,13,7,14]
array2 = [1,13,15,7]
#looping through the first array
for i in array1:
    #checking for same in second list
    if i in array2:
        # append it to empty list
        output.append(i)
# sorting to print in ascending order
output = sorted(output)
print("The numbers that are common in both the arrays is ",output)